from dataclasses import dataclass
import datetime
from typing import List
from check_funktion import check_type


@dataclass
class Driver:
    name: str = ''
    team: str = ''
    abbreviation: str = ''
    start_time: object = None
    end_time: object = None
    lap_time: object = None
    count_driver = 0
    incorrect_logged_drivers = []

    def abbreviations_decoding(self, driver_abr_string: str) -> None:
        check_type(string=driver_abr_string)
        self.abbreviation, self.name, self.team = driver_abr_string.split('_')

    def prepare_time_string(self, log_list: List[str]) -> str:
        for driver_string in log_list:
            if self.abbreviation in driver_string:
                clear_data_list = driver_string.strip(self.abbreviation)
                datetime_string = clear_data_list.replace('_', ' ')
                return datetime_string

    def string_to_time(self, log_list: List[str]) -> datetime.datetime:
        datetime_string = self.prepare_time_string(log_list=log_list)
        datetime_object = datetime.datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S.%f')
        return datetime_object

    def get_time(self, start_time_list: List[str], end_time_list: List[str]) -> None:
        start_time = self.string_to_time(log_list=start_time_list)
        self.start_time = start_time
        end_time = self.string_to_time(log_list=end_time_list)
        self.end_time = end_time

    def calculate_lap_time(self) -> None:
        if self.end_time > self.start_time:
            self.lap_time = self.end_time - self.start_time
        else:
            Driver.incorrect_logged_drivers.append(self)

    def add_attributes(self, driver_abr_string: str, start_time_list: List[str], end_time_list: List[str]) -> None:
        self.abbreviations_decoding(driver_abr_string=driver_abr_string)
        self.get_time(start_time_list=start_time_list, end_time_list=end_time_list)
        self.calculate_lap_time()
        Driver.count_driver += 1

    def __repr__(self) -> str:
        return f'{self.name} | {self.team} | {self.lap_time}'
