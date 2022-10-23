from utils import check_type


class Driver:
    def __init__(self):
        self.abbr = None
        self.name = None
        self.team = None

    def abbreviations_decoding(self, driver_abr_string: str):
        check_type(string=driver_abr_string)
        self.abbr, self.name, self.team = driver_abr_string.split('_')