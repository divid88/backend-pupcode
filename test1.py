import unittest
from unittest.mock import patch



class TestPrint(unittest.TestCase):
    
    @patch('builtins.print')

    def test_program(self, mock_print):

        with open('./main.py') as f:
            exec(f.read())

        mock_print.assert_called_with("Hello World!")

if __name__ == '__main__':
    unittest.main()