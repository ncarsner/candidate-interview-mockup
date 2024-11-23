"""Unit tests for the questions logic.
"""

import unittest
from question_cli.questions import get_random_question

class TestQuestions(unittest.TestCase):

    def test_get_random_question(self):
        question = get_random_question('developer')
        self.assertIn('developer', question['roles'])

if __name__ == '__main__':
    unittest.main()