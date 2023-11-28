import unittest
from unittest.mock import patch
from app import rm, FileNotFoundError


class MockTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.file = 'testfile.py'
    
    @patch('app.os.remove')
    @patch('app.os.path.isfile')
    def test_rm_if_file_exists(self, mocked_isfile, mocked_remove):
        mocked_isfile.return_value = True
        
        rm(self.file)
        mocked_remove.assert_called_with(self.file)
            
    @patch('app.os.remove')
    @patch('app.os.path.isfile')
    def test_rm_if_file_deos_not_exist(self, mocked_isfile, mocked_remove):

        mocked_isfile.return_value = False
        with self.assertRaises(FileNotFoundError):
            rm(self.file)
        mocked_remove.assert_not_called()

