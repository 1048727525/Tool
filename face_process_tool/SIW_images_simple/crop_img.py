import os
import argparse
import re
import cv2
import math
from multiprocessing import Process
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

def make_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def crop_face_from_scene(image,face_name_full, scale):
    f=open(face_name_full,'r')
    lines=f.readlines()
    y1,x1,w,h=[float(ele) for ele in lines[:4]]
    f.close()
    y2=y1+w
    x2=x1+h

    y_mid=(y1+y2)/2.0
    x_mid=(x1+x2)/2.0
    h_img, w_img = image.shape[0], image.shape[1]
    #w_img,h_img=image.size
    w_scale=scale*w
    h_scale=scale*h
    y1=y_mid-w_scale/2.0
    x1=x_mid-h_scale/2.0
    y2=y_mid+w_scale/2.0
    x2=x_mid+h_scale/2.0
    y1=max(math.floor(y1),0)
    x1=max(math.floor(x1),0)
    y2=min(math.floor(y2),w_img)
    x2=min(math.floor(x2),h_img)
    region=image[x1:x2,y1:y2]
    return region

def main(args):
    src_root_dir = args.src_root_dir
    dst_root_dir = args.dst_root_dir
    scale = args.scale
    def son_process(img_path_list):
        make_dir(dst_root_dir)
        sum_img = len(img_path_list)
        for idx, img_path in enumerate(img_path_list):
            bbox_path = img_path.replace(img_path.split(".")[-1], "dat")
            #full_name = re.match('./(.+)', img_path).group(1)
            full_name = img_path.lstrip("./")
            depth_path = os.path.join("./Depth", full_name).replace(".jpg", "_depth.jpg")

            if os.path.exists(img_path) and os.path.exists(bbox_path) and os.path.exists(depth_path):
                dst_img = os.path.join(dst_root_dir, full_name)
                dst_depth_img = os.path.join(dst_root_dir, "Depth", full_name.replace(".jpg", "_depth.jpg"))
                if os.path.exists(dst_img) and os.path.exists(dst_depth_img):
                    continue
                make_dir(os.path.dirname(dst_img))
                make_dir(os.path.dirname(dst_depth_img))
                img = cv2.imread(img_path)
                img_depth = cv2.imread(depth_path)
                img_crop = crop_face_from_scene(img, bbox_path, scale)
                depth_crop = crop_face_from_scene(img_depth, bbox_path, scale)
                cv2.imwrite(dst_img, img_crop)
                cv2.imwrite(dst_depth_img, depth_crop)
                print("[{}/{}]writing {}, {}".format(idx, sum_img, dst_img, dst_depth_img))
            else:
                print("data shotage, skip")
                continue
        print("finish")
    
    all_img_path_list = []
    listdir(src_root_dir, all_img_path_list, [".jpg"])
    son_num = 5
    patch_list = split_list(all_img_path_list, son_num)
    print("sum of son process: {}".format(len(patch_list)))
    print("average lenth in son process: {}".format(len(all_img_path_list)//son_num))

    process_list = []
    for i in range(len(patch_list)):
        p = Process(target=son_process, args=(patch_list[i],))
        process_list.append(p)
    for p in process_list:
        p.start()

        

def help_replace(path):
    img_list = []
    listdir(path, img_list, [".jpg"])
    for img_path in img_list:
        dst_path = img_path.replace("_scene.jpg", "_depth1D.jpg")
        os.rename(img_path, dst_path)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="crop face images")
    parser.add_argument('--src_root_dir', type=str, default="./Test/live", help="root dir of src images")
    parser.add_argument('--dst_root_dir', type=str, default="../SiW_images_crop", help="dst dir of src images")
    parser.add_argument('--scale', type=float, default=1.5, help="the scale of crop face")
    args = parser.parse_args()
    main(args)
    #help_replace("/home/wangzhuo/data/oulu_images_crop/Depth")