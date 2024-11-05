import unittest
from unittest.mock import patch
import main_program

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '85', '90', '95'])
    @patch('builtins.print')
    def test_main_valid_input(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('The class average is: 90.00')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )

    @patch('builtins.input', side_effect=['0','3', '85', '90', '95'])
    @patch('builtins.print')
    def test_invalid_number_of_students(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('The class average is: 90.00')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )

    @patch('builtins.input', side_effect=['3', '105', '85', '-5', '90', '95'])
    @patch('builtins.print')
    def test_invalid_grades(self, mock_print, mock_input):
        main_program.main()
        mock_print.assert_called_with('The class average is: 90.00')
        self.assertIn(
            unittest.mock.call('The class average is: 90.00'), 
            mock_print.mock_calls
        )

   


if __name__ == "__main__":
    unittest.main()
