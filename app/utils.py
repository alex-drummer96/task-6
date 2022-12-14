import os
from typing import List
from class_driver import Driver
from check_funktion import check_filepath


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
