class S3UploadloderExecption(Exception):
    def __init__(self, msg):
        self.msg = msg


class SnowflakeExecption(Exception):
    def __init__(self, msg):
        self.msg = msg
