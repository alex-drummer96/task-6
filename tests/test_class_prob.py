import unittest
from app.prob import AnonymousSurvey


class TestAnonymous(unittest.TestCase):

    def setUp(self) -> None:
        question = 'ШО?'
        self.my_survey = AnonymousSurvey(question=question)

    def test_store_single(self):
        self.my_survey.store_response(new_response='НИШО')
        self.assertIn('НИШО', self.my_survey.responses)
