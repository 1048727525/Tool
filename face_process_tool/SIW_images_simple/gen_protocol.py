import os
import re
def listdir(path, list_name, type_list):
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name, type_list) 
        elif os.path.splitext(file_path)[1] in type_list:  
            list_name.append(file_path)
def make_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


if __name__ == "__main__":
    