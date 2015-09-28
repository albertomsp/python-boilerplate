import os

# Usage: in the files you need environment variables:
# from config.env import ENV
# print ENV.ENV1
# print ENV.ENV2


class EnvironmentVariables:

    def __init__(self):
        PY_ENV = os.getenv('PY_ENV', 'development')

        env_list = {
            'production': {
                'ENV1': os.getenv('PRODUCTION_ENV1'),
                'ENV2': os.getenv('PRODUCTION_ENV2')
            },
            'development': {
                'ENV1': os.getenv('DEVELOPMENT_ENV1'),
                'ENV2': os.getenv('DEVELOPMENT_ENV2')
            },
            'testing': {
                'ENV1': os.getenv('TESTING_ENV1'),
                'ENV2': os.getenv('TESTING_ENV2')
            }
        }

        # Each entry in env_list[PY_ENV] will be assigned to a class variable
        # self.ENV1 = "value"
        for e, v in env_list[PY_ENV].items():
            setattr(self, e, v)

            # Equivalent:
            # exec('self.' + e + ' = "' + str(v) + '"') # Build the python code
            # and exec

ENV = EnvironmentVariables()
