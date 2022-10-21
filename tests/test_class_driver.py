from app.class_driver import Driver
import unittest
from unittest.mock import patch


class TestDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = Driver()

    @patch('app.check_funktion.check_filepath', return_value=None)
    def test_abr_decoding(self, mock_check):
        test_string = 'DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER'
        abbreviation, name, team = test_string.split('_')
        self.driver.abbreviations_decoding(driver_abr_string=test_string)
        self.assertEqual(first=self.driver.abbreviation, second=abbreviation)
        self.assertEqual(first=self.driver.name, second=name)
        self.assertEqual(first=self.driver.team, second=team)


