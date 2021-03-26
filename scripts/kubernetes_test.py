import logging
import os
import re
import subprocess
from datetime import datetime, timedelta
from kubernetes import client, config
from kubernetes.client import ApiClient, CoreV1Api, AppsV1Api
from kubernetes import config, client
from kubernetes.client.models import AppsV1beta1Deployment, V1Container, V1EnvVar, V1EnvVarSource, V1SecretKeySelector

format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
datefmt = '%d-%m-%Y %H:%M:%S'
logging.basicConfig(format=format, level=logging.DEBUG, datefmt=datefmt)
logger = logging.getLogger('kubernetes-logs')

# get pods list
# def get_pods():
#     config.load_kube_config()
#     v1 = client.CoreV1Api()
#     pod_list = v1.list_namespaced_pod("astronomer-optical-transit-7722")
#     for pod in pod_list.items:
#         print("%s\t%s\t%s" % (pod.metadata.name,
#                               pod.status.phase,
#                               pod.status.pod_ip))

# get_pods()

# ENV_VAR = {'TEST': 'TEST'}


# def get_kubernetes_client(apps):
#     if apps:
#         return _get_client_apps_api()
#     else:
#         return _get_client_core_api()


# def _get_client_core_api() -> CoreV1Api:
#     return CoreV1Api(ApiClient())


# def _get_client_apps_api() -> AppsV1Api:
#     return AppsV1Api(ApiClient())


# def create_kubernetes_secret(kube_client: CoreV1Api, secret: ENV_VAR, namespace_arg: str):
#     secret_key, secret_value = ENV_VAR.items()

#     secret_metadata = client.V1ObjectMeta(
#         name=secret_key, namespace=namespace_arg)

#     data = {secret_key: secret_value}

#     body = client.V1Secret(api_version='v1', kind='Secret',
#                            string_data=data, metadata=secret_metadata)


# format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
# datefmt = '%d-%m-%Y %H:%M:%S'
# logging.basicConfig(format=format, level=logging.DEBUG, datefmt=datefmt)
# logger = logging.getLogger('config_integrator_logger')

# LABEL_SELECTOR = 'platform,workspace,platform-release'

# DAYS_RETENTION = int(os.getenv('DAYS_RETENTION', 20))

# def get_pods():

#     v1 = client.CoreV1Api()
#     pod_list = v1.list_namespaced_pod("example")
#     for pod in pod_list.items:
#         print("%s\t%s\t%s" % (pod.metadata.name,
#                               pod.status.phase,
#                               pod.status.pod_ip))

# def get_namespace_names(api_client, label_selector):
#     logger.info('getting namespaces')
#     request = client.CoreV1Api(api_client).list_namespace(
#         label_selector=label_selector).to_dict().get('items', '')
#     airflow_namespaces = [namespace['metadata']['name']
#                           for namespace in request]
#     return airflow_namespaces


# def get_deployments_within_namespace(api_client, namespace):
#     logger.info('Geting deployments')
#     deployments = client.AppsV1Api(api_client).list_namespaced_deployment(
#         namespace).to_dict().get('items', '')
#     return deployments


# def get_deployment_modify_time(deployment_dict: dict) -> datetime:
#     logger.info('Extracting last_update_time from deployment')
#     try:
#         return deployment_dict['status']['conditions'][0]['last_update_time']
#     except KeyError:
#         logger.warning('No specified last_update_time')
#         raise


# def localize_datetimes(unlocalized_datetime: datetime) -> datetime:
#     localized_datetime = unlocalized_datetime.replace(tzinfo=None)
#     return localized_datetime


# def authorize_astro_cli(domain, api_key):
#     logger.info('Authorize in astro')
#     bashCommand = f'logger.infof "{api_key}\n\n" | astro auth login {domain} --oauth'

#     process = subprocess.run(
#         bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     if process.stderr.decode():
#         logging.error(process.stderr.decode())
#         raise RuntimeError("Couldnt login to astronomer.")


# def escape_ansi(line):
#     ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
#     return ansi_escape.sub('', line)


# def parse_cli_list(stdout, key_position=0, return_value_position=1) -> dict:
#     raw_list = escape_ansi(stdout.decode()).split('\n')
#     split_output = [line.strip().split() for line in raw_list[1:]]
#     objects = {line[key_position]: line[return_value_position]
#                for line in split_output if len(line) > 1}
#     return objects


# def get_astro_deployment_id(deployment_name):
#     logger.info(f'getting deployment id from astro for {deployment_name}')
#     process = subprocess.run(
#         'astro deployment list', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     deployments = parse_cli_list(
#         process.stdout, key_position=1, return_value_position=3)
#     if deployment_name.startswith('astronomer-'):
#         deployment_name = '-'.join(deployment_name.split('-')[1:])
#     current_deployment = deployments.get(deployment_name)
#     return current_deployment


# def delete_astro_deployment(deployment_id):
#     logger.info(f'deleting astro deployment {deployment_id}')
#     process = subprocess.run([
#         "astro", "deployment", "delete", deployment_id
#     ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     if 'Successfully created deployment' in process.stdout.decode():
#         logger.info(f'Successfully deleted deployment {deployment_id}')
#     else:
#         logger.error(process.stdout.decode())
#         logger.error(process.stderr.decode())


# def main():
#     logger.info('loading kubeconfig')
#     config.load_incluster_config()
#     api_client = client.ApiClient()
#     airflow_namespaces = get_namespace_names(api_client, LABEL_SELECTOR)
#     domain = os.getenv('ASTRO_DOMAIN')
#     api_key = os.getenv('API_KEY')

#     authorize_astro_cli(domain, api_key)
#     for airflow_namespace in airflow_namespaces:
#         kube_deployments = get_deployments_within_namespace(
#             api_client, airflow_namespace)
#         worker_deployment = [deployment for deployment in kube_deployments if deployment['metadata']['labels'][
#             'component'] == 'worker'][0]
#         try:
#             last_update_time = get_deployment_modify_time(worker_deployment)
#         except KeyError:
#             continue
#         if localize_datetimes(last_update_time) < localize_datetimes(datetime.now() - timedelta(days=DAYS_RETENTION)):
#             deployment_id = get_astro_deployment_id(airflow_namespace)
#             delete_astro_deployment(deployment_id)


# if __name__ == '__main__':
#     main()
