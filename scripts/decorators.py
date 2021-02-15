from functools import wraps
import time
import logging


def logging_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            logging.info('Task starting')
            result = func(self, *args, **kwargs)
            logging.info('Task finished')
            return result
        except BaseException as ex:
            logging.error("Execution failed with {}".format(ex))
            raise ex
        return wrapper
