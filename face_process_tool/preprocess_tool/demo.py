import os
def listdir(path, list_name, type_list):
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name, type_list) 
        elif os.path.splitext(file_path)[1] in type_list:  
            list_name.append(file_path)

img_path_list = []
dat_path_list = []
listdir("../SiW_images/Train_60", img_path_list, [".jpg"])
listdir("../SiW_images/Train_60", dat_path_list, [".dat"])
for img_path in img_path_list:
    if int(img_path.split(".")[-2].split("_")[-1])>59:
        os.remove(img_path)

for dat_path in dat_path_list:
    if int(dat_path.split(".")[-2].split("_")[-1])>59:
        os.remove(dat_path)