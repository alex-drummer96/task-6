import unittest
from main import my_class
from main import utils


class TestDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = my_class.Driver()

    def test_abbr_decoding_typical(self):
        test_case = 'DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER'
        abbr, name, team = test_case.split('_')
        self.driver.abbreviations_decoding(driver_abr_string=test_case)
        self.assertEqual(first=self.driver.abbr, second=abbr)
        self.assertEqual(first=self.driver.name, second=name)
        self.assertEqual(first=self.driver.team, second=team)

    def test_abbr_decoding_atypical(self):
        test_cases = [1, {1: 'str'}, [1, 'str']]
        for test_case in test_cases:
            with self.subTest(string=test_case):
                self.assertRaises(utils.CustomTypeError, self.driver.abbreviations_decoding, test_case)
