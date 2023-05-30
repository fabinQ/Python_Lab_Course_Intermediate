import os
import functools
from datetime import datetime as dt

def path_to_fileLog (file_name):
    path = os.getcwd()
    if file_name [-4:] == ".txt":
        path = os.path.join(path,file_name)
    else:
        path = os.path.join(path,file_name+".txt")
    return path

def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            result = func(path)
            file = open(log_file_path, "a")
            file.write("Action {} executed on {} on {}".format(logged_action, log_file_path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            file.write('\n')
            return result
        return the_real_wrapper
    return wrapper_with_log_to_known_file

@wrapper_with_log_file("create_file", path_to_fileLog("create_file.txt"))
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@wrapper_with_log_file("delete_file",path_to_fileLog("delete_file"))
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)

path = path_to_fileLog("dummy_file")
create_file(path)
delete_file(path)
create_file(path)
delete_file(path)
