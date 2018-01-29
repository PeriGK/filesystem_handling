import unittest
from unittest import mock
from fs_handler_main import *

class FileSystemHandlerTest(unittest.TestCase):

    def setUp(self):
        """setUp is run before each test case. It is usually used to setup(wow) some common values
        for all test cases"""
        print('setUp: Initialize instance variables')
        self.directory = '/home/periklis/'
        self.new_filename = 'dummy_new_filename.txt'

        # Fun fact: The os module we are using is indirectly imported from fs_handler_main
        self.full_path = os.path.join(self.directory, self.new_filename)

    def tearDown(self):
        # This is something not very useful, it is only written this way to demonstrate how tearDown works
        print('tearDown: Reset instance variables')
        self.directory = ''
        self.new_filename = ''

    @mock.patch('builtins.open', mock=mock.mock_open)
    @mock.patch('fs_handler_main.check_file_exists')
    @mock.patch('fs_handler_main.check_dir_exists')
    def test_create_file_success(self, mock_check_dir_exists, mock_check_file_exists, mock_open_func):
        print('test_create_file_success')
        mock_check_dir_exists.return_value = True
        mock_check_file_exists.return_value = False
        self.assertTrue(create_file(self.directory, self.new_filename))

    @mock.patch('builtins.open', mock=mock.mock_open)
    @mock.patch('fs_handler_main.check_file_exists')
    @mock.patch('fs_handler_main.check_dir_exists')
    def test_create_file_failure_dir_no_exists(self, mock_check_dir_exists, mock_check_file_exists, mock_open_func):
        print('test_create_file_failure_dir_no_exists')
        mock_check_dir_exists.return_value = False
        mock_check_file_exists.return_value = False
        self.assertFalse(create_file(self.directory, self.new_filename))

    @mock.patch('builtins.open', mock=mock.mock_open)
    @mock.patch('fs_handler_main.check_file_exists')
    @mock.patch('fs_handler_main.check_dir_exists')
    def test_create_file_failure_file_already_exists(self, mock_check_dir_exists, mock_check_file_exists, mock_open_func):
        print('test_create_file_failure_file_already_exists')
        mock_check_dir_exists.return_value = False
        mock_check_file_exists.return_value = False
        self.assertFalse(create_file(self.directory, self.new_filename))

    # We mock the fs_handler_main.os.* modules, if we mock the os provided from python directly, it will not work
    @mock.patch('fs_handler_main.os.path.isfile')
    @mock.patch('fs_handler_main.os.remove')
    def test_delete_file_success(self, mock_os_remove, mock_os_is_file):
        print('test_delete_file_success')
        mock_os_is_file.return_value = True
        delete_file(self.full_path)
        mock_os_remove.assert_called_with(self.full_path)

    @mock.patch('fs_handler_main.os.path.isfile')
    @mock.patch('fs_handler_main.os.remove')
    def test_delete_file_failure_not_found(self, mock_os_remove, mock_os_is_file):
        print('test_delete_file_failure_not_found')
        mock_os_is_file.return_value = False
        full_path = os.path.join(self.directory, self.new_filename)
        delete_file(full_path)
        mock_os_remove.assert_not_called()

    @mock.patch('fs_handler_main.os.path.isfile')
    @mock.patch('fs_handler_main.os.remove')
    def test_delete_file_failure_permission_error(self, mock_os_remove, mock_os_is_file):
        print('test_delete_file_failure_permission_error')
        self.directory = '/etc/'
        self.new_filename = 'resolv.conf'
        mock_os_is_file.return_value = True
        full_path = os.path.join(self.directory, self.new_filename)
        self.assertRaises(PermissionError, delete_file(full_path))

    @mock.patch('fs_handler_main.os.path.isfile')
    def test_check_file_exists_success(self, mock_os_is_file):
        print('test_check_file_exists_success')
        mock_os_is_file.return_value = True
        self.assertTrue(check_file_exists(self.new_filename))
        mock_os_is_file.assert_called_with(self.new_filename)

    @mock.patch('fs_handler_main.os.path.isfile')
    def test_check_file_exists_failure(self, mock_os_is_file):
        print('test_check_file_exists_failure')
        mock_os_is_file.return_value = False
        self.assertFalse(check_file_exists(self.new_filename))
        mock_os_is_file.assert_called_with(self.new_filename)

    @mock.patch('fs_handler_main.os.path.exists')
    def test_check_dir_exists_success(self, mock_os_dir_exists):
        print('test_check_dir_exists_success')
        mock_os_dir_exists.return_value = True
        self.assertTrue(check_dir_exists(self.directory))
        mock_os_dir_exists.assert_called_with(self.directory)

    @mock.patch('fs_handler_main.os.path.exists')
    def test_check_dir_exists_failure(self, mock_os_dir_exists):
        print('test_check_dir_exists_failure')
        mock_os_dir_exists.return_value = False
        self.assertFalse(check_dir_exists(self.directory))
        mock_os_dir_exists.assert_called_with(self.directory)
