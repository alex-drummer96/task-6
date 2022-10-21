from utils import path_dispatcher, open_file, sort_drivers
from class_driver import Driver
from typing import List


def build_report(dir_path: str) -> List[Driver]:
    drivers = []
    path_list = path_dispatcher(dir_path=dir_path)
    driver_abr_list = open_file(filepath=path_list[0])
    start_time_list = open_file(filepath=path_list[2])
    end_time_list = open_file(filepath=path_list[1])
    for driver_abr_string in driver_abr_list:
        driver = Driver()
        driver.add_attributes(driver_abr_string=driver_abr_string,
                              start_time_list=start_time_list, end_time_list=end_time_list)
        if not driver.lap_time is None:
            drivers.append(driver)
    return drivers


def print_report(dir_path: str) -> None:
    count = 1
    sorted_drivers_list = sort_drivers(drivers_list=build_report(dir_path=dir_path))
    for driver in sorted_drivers_list:
        if count != 15:
            print(f'{count}. {driver}')
            count += 1
        else:
            print(f'{count}. {driver} \n ------------------------------------------------------------')
            count += 1
    if len(Driver.incorrect_logged_drivers) > 0:
        for driver in Driver.incorrect_logged_drivers:
            print(f'{count}. {driver} This driver has incorrect log data')
            count += 1
