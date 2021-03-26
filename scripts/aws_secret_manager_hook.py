import base64
import logging
from ast import literal_eval

from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.exceptions import AirflowException
from botocore.exceptions import ClientError
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class AwsSecretsManagerHook(AwsHook):
    def __init__(self,
                 aws_secret_name,
                 **kwargs):
        super().__init__(**kwargs)
        self.aws_secret_name = aws_secret_name

    def get_conn(self):
        return self.get_client_type('secretsmanager', region_name='us-east-1')

    def _get_secret(self):
        try:
            get_secret_value_response = self.get_conn().get_secret_value(
                SecretId=self.aws_secret_name
            )
        except ClientError as err:
            self.log.error(str(err))
            if err.response['Error']['Code'] == 'ResourceNotFoundException':
                logging.error("The requested secret " +
                              self.aws_secret_name + " was not found")
            elif err.response['Error']['Code'] == 'InvalidRequestException':
                logging.error("The request was invalid due to:", err)
            elif err.response['Error']['Code'] == 'InvalidParameterException':
                logging.error("The request had invalid params:", err)
            raise AirflowException('Error: {}'.format(str(err)))
        else:
            return get_secret_value_response['SecretString'] \
                if 'SecretString' in get_secret_value_response \
                else get_secret_value_response['SecretBinary']

    def get_secrets_dict(self):
        secret = self._get_secret()
        if isinstance(secret, str):
            secret = literal_eval(secret)
        return secret


class AwsSecretManagerMixin():

    def get_fernet_function(self, secret_key, secret_salt):
        return self._create_fernet(secret_key, secret_salt)

    def _create_fernet(self, secret_key, secret_salt):
        if not isinstance(secret_salt, bytes):
            secret_salt = bytes(secret_salt, encoding='utf8')
        if not isinstance(secret_key, bytes):
            secret_key = bytes(secret_key, encoding='utf8')
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=secret_salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(secret_key))
        fernet_function = Fernet(key)
        return fernet_function

    def decrypt_data(self, value, fernet_function):
        if value is None:
            return value
        else:
            if not isinstance(value, bytes):
                value = bytes(value, encoding='utf-8')
            return fernet_function.decrypt(value).decode('utf-8')

    def encrypt_data(self, value, fernet_function):
        if value is None:
            return value
        else:
            if not isinstance(value, bytes):
                value = bytes(value, encoding='utf-8')
            return fernet_function.encrypt(value).decode('utf-8')
