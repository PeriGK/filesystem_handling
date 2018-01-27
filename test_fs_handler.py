import unittest
from unittest import mock
from fs_handler_main import *


class FileSystemHandlerTest(unittest.TestCase):

    def setUp(self):
        """setUp is run before each test case. It is usually used to setup - wow - some common values
        for all test cases"""
        self.directory = '/home/periklis/'
        self.new_filename = 'dummy_new_filename.txt'

        # Fun fact: The os module we are using is indirectly imported from fs_handler_main
        self.full_path = os.path.join(self.directory, self.new_filename)

    def tearDown(self):
        """tearDown is used to do the opposite to setUp, clean up or reset any variables
        It is only added here for demonstration."""
        pass

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
        delete_file(self.full_path)
        mock_os_remove.assert_called_with(self.full_path)

    @mock.patch('fs_handler_main.os.path.isfile')
    @mock.patch('fs_handler_main.os.remove')
    def test_delete_file_failure_not_found(self, mock_os_remove, mock_os_is_file):
        mock_os_is_file.return_value = False
        full_path = os.path.join(self.directory, self.new_filename)
        delete_file(full_path)
        mock_os_remove.assert_not_called()

    @mock.patch('fs_handler_main.os.path.isfile')
    def test_check_file_exists_success(self, mock_os_is_file):
        mock_os_is_file.return_value = True
        self.assertTrue(check_file_exists(self.new_filename))
        mock_os_is_file.assert_called_with(self.new_filename)

    @mock.patch('fs_handler_main.os.path.isfile')
    def test_check_file_exists_failure(self, mock_os_is_file):
        mock_os_is_file.return_value = False
        self.assertFalse(check_file_exists(self.new_filename))
        mock_os_is_file.assert_called_with(self.new_filename)
