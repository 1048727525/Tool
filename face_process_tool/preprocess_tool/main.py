#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/01/02 22:34:53
@Author  :   Zhuo Wang 
@Version :   1.0
@Contact :   1048727525@qq.com
'''
from align.detector import detector_mtcnn
from utils import *
import cv2
import shutil
import torch
import argparse
from PIL import Image
import os
from multiprocessing import Process
import threading
def sort_help(elem):
    return (elem[2]-elem[0])*(elem[3]-elem[1])

def img2dat(device_id, img_path_list):
    face_detector = detector_mtcnn(torch.device("cuda:{}".format(device_id)))
    img_sum = len(img_path_list)
    for idx, img_path in enumerate(img_path_list):
        img = cv2.imread(img_path)
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        dat_path = img_path.replace("jpg", "dat")
        if os.path.exists(dat_path):
            os.remove(dat_path)
        try:
            bounding_boxes, landmarks = face_detector.detect_faces(img)
            list(bounding_boxes).sort(key=sort_help, reverse=True)
            bounding_box = bounding_boxes[0]
            '''
            w = max(int(bounding_box[2]-bounding_box[0]), int(bounding_box[3]-bounding_box[1]))
            h = w
            '''
            w = int(bounding_box[2]-bounding_box[0])
            h = int(bounding_box[3]-bounding_box[1])
            x1 = int((bounding_box[0]+bounding_box[2])//2-0.5*w)
            y1 = int((bounding_box[1]+bounding_box[3])//2-0.5*h)
            record = [x1, y1, w, h]
        except:
            print("pass")
            continue
        with open(dat_path, 'w') as write_file:
            for i in range(4):
                write_file.write(str(record[i]))
                write_file.write('\n')
        print("[{}/{}]writing {}".format(idx+1, img_sum, dat_path))
    print("finish")

        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="dat from img")
    parser.add_argument('--src_dir', type=str, default="/ssd1/wangzhuo/data/img_MSU_MFSD/real/real_client009_android_SD_scene01/", help="root dir of images")
    parser.add_argument('--gpu', type=str, default="1", help="set gpu num")
    args = parser.parse_args()

    img_path_list = []
    listdir(args.src_dir, img_path_list, [".jpg"])
    # single-process
    #img2dat(args.gpu, args.src_dir)

    # muti-processes
    processes_num = 5
    son_list = split_list(img_path_list, processes_num)
    print("sum of son process: {}".format(len(son_list)))
    print("average lenth in son process: {}".format(len(img_path_list)//processes_num))

    process_list = []
    for i in range(len(son_list)):
        p = Process(target=img2dat, args=(args.gpu,son_list[i],))
        process_list.append(p)
    for p in process_list:
        p.start()