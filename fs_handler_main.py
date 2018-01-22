import os


def create_file(target_directory, new_file_name):
    if check_dir_exists(target_directory) and not check_file_exists(new_file_name):
        new_file_name = os.path.join(target_directory, new_file_name)
        with open(new_file_name, 'w') as f:
            f.write('')
        return True
    return False


def check_dir_exists(target_directory):
    return os.path.exists(target_directory)


def check_file_exists(new_file_name):
    return os.path.isfile(new_file_name)


create_file('/home/myhome/', 'hello_fs.txt')