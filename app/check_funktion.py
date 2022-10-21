import os


class CustomTypeError(Exception):

    def __init__(self, data_type):
        self.data_type = data_type

    def __str__(self):
        return f'{self.data_type} is not allowed. Only string'


def check_type(string: str):
    if not isinstance(string, str):
        return CustomTypeError(type(string))


class MyException(Exception):
    pass


def check_filepath(filepath: str) -> None:
    if not os.path.isfile(filepath):
        raise MyException(f'{filepath} is not a file path')
