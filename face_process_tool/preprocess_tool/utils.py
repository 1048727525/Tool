import os
def listdir(path, list_name, type_list):
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name, type_list) 
        elif os.path.splitext(file_path)[1] in type_list:  
            list_name.append(file_path)

def split_list(father_list, num):
    '''
    num: the numbers of son list splited from father list 
    '''
    res = []
    average_lenth = len(father_list)//num
    start_index = 0
    while(start_index+average_lenth<len(father_list)):
        res.append(father_list[start_index:start_index+average_lenth])
        start_index = start_index + average_lenth
    res.append(father_list[start_index:])
    return res