import unittest
from unittest import mock
from fs_handler_main import *


class FileSystemHandlerTest(unittest.TestCase):

    def setUp(self):
        """setUp is run before each test case. It is usually used to setup(dont tell me :P) some common values
        for all test cases"""
        self.directory = '/home/periklis/'
        self.new_filename = 'dummy_new_filename.txt'

    # TODO: Adjust it to assert mock open and write were called
    @mock.patch('fs_handler_main.check_file_exists')
    @mock.patch('fs_handler_main.check_dir_exists')
    def test_create_file_success(self, mock_check_dir_exists, mock_check_file_exists):
        mock_check_dir_exists.return_value = True
        mock_check_file_exists.return_value = False
        self.assertTrue(create_file(self.directory, self.new_filename))

    @mock.patch('fs_handler_main.os.path.isfile')
    @mock.patch('fs_handler_main.os.remove')
    def test_delete_file_success(self, mock_os_remove, mock_os_is_file):
        mock_os_is_file.return_value = True
        full_path = os.path.join(self.directory, self.new_filename)
        delete_file(full_path)
        mock_os_remove.assert_called_with(full_path)

    @mock.patch('fs_handler_main.os.path.isfile')
    @mock.patch('fs_handler_main.os.remove')
    def test_delete_file_failure_not_found(self, mock_os_remove, mock_os_is_file):
        mock_os_is_file.return_value = False
        full_path = os.path.join(self.directory, self.new_filename)
        delete_file(full_path)
        mock_os_remove.assert_not_called()
