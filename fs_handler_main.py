import os


def create_file(target_directory, new_file_name):
    if check_dir_exists(target_directory) and not check_file_exists(new_file_name):
        new_file_name = os.path.join(target_directory, new_file_name)
        with open(new_file_name, 'w') as f:
            f.write('')
        return True
    return False


def delete_file(full_path_to_file):
    if os.path.isfile(full_path_to_file):
        os.remove(full_path_to_file)


def check_dir_exists(target_directory):
    return os.path.exists(target_directory)


def check_file_exists(new_file_name):
    return os.path.isfile(new_file_name)


# Execute this, only if the script is invoked directly from the command line
if __name__ == '__main__':
    path = '/home/periklis/'
    filename = 'hello_fs.txt'
    create_file(path, filename)
    delete_file(os.path.join(path, filename))
