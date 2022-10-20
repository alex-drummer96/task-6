import os
from typing import List
from app import Driver


class MyException(Exception):
    pass


def check_filepath(filepath: str) -> None:
    if not os.path.isfile(filepath):
        raise MyException(f'{filepath} is not a file path')


def open_file(filepath: str) -> List[str]:
    check_filepath(filepath=filepath)
    with open(filepath) as file:
        text = file.read()
        return text.split('\n')


def sort_drivers(drivers_list) -> List[Driver]:
    return sorted(drivers_list, key=lambda x: x.lap_time, reverse=True)


def path_dispatcher(dir_path: str) -> List[str]:
    file_list = os.listdir(path=dir_path)
    path_list = []
    for file in file_list:
        filepath = os.path.join(dir_path, file)
        path_list.append(filepath)
    return path_list
