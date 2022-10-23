class CustomTypeError(Exception):

    def __init__(self, data_type):
        self.data_type = data_type

    def __str__(self):
        return f'{self.data_type} is not allowed. Only string'


def check_type(string):
    if not isinstance(string, str):
        raise CustomTypeError(type(string))
