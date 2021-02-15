from os import getenv


class EnvRetriever:
    """
    class to retrieve environment variable
    """

    def __init__(self, var_name):
        self.var_name = var_name

    def __call__(self, *args, **kwargs):
        return self._get_variable(self.var_name)

    def _get_variable(self, var_name):
        var = getenv(var_name)
        if var is None:
            raise EnvironmentError('{} env var is not found.'.format(var_name))
        return var


test_var = EnvRetriever('hi')
print(test_var())
