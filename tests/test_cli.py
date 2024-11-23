"""Unit tests for the CLI logic.
"""
import unittest
from unittest.mock import patch
from question_cli.question_cli import run

class TestCLI(unittest.TestCase):

    @patch('builtins.input', return_value='developer')
    @patch('builtins.print')
    def test_run(self, mock_print, mock_input):
        run()
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()