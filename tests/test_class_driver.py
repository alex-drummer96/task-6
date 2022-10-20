from app.app import Driver
import unittest


class TestDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = Driver()

    def test_abr_decoding_expected(self):
        test_string = 'DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER'
        test_answer = test_string.split('_')
        self.driver.abbreviations_decoding(driver_abr_string=test_string)
        self.assertEqual(first=self.driver.abbreviation, second=test_answer[0])
        self.assertEqual(first=self.driver.name, second=test_answer[1])
        self.assertEqual(first=self.driver.team, second=test_answer[2])

    def test_abr_decoding_unexpected(self):
        test_cases = [123, ['DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER'], True]
