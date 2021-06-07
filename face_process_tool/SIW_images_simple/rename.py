import os
import re

video_path_list = []
def listdir(path, list_name, type_list):
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name, type_list) 
        elif os.path.splitext(file_path)[1] in type_list:  
            list_name.append(file_path)

def help_func(s):
    return int(s.split("_")[-1].rstrip(".jpg"))

img_path_list = []
listdir("../SiW_images_crop/Train_60", img_path_list, [".jpg"])
for img_path in img_path_list:
    video_path = os.path.dirname(img_path)
    if not (video_path in video_path_list):
        video_path_list.append(video_path)
for video_path in video_path_list:
    img_list = os.listdir(video_path)
    img_list.sort(key=help_func)
    img_n = 0
    for img_name in img_list:
        img_path = os.path.join(video_path, img_name)
        dst_img_path = os.path.join(video_path, img_name.rstrip(img_name.split("_")[-1])+"{}.jpg".format(img_n))
        
        os.rename(img_path, dst_img_path)
        img_n += 1
