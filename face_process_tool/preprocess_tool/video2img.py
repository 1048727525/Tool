#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   video2img.py
@Time    :   2020/12/31 09:40:02
@Author  :   Zhuo Wang 
@Version :   1.0
@Contact :   1048727525@qq.com
'''

import sys
from align.detector import detector_mtcnn
from PIL import Image
from glob import glob
import os
import cv2
import argparse
import torch
from multiprocessing import Process
import random
def make_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def sort_help(elem):
    return (elem[2]-elem[0])*(elem[3]-elem[1])

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

def listdir(path, list_name, type_list):
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name, type_list) 
        elif os.path.splitext(file_path)[1] in type_list:  
            list_name.append(file_path)

def main(args):
    # defaut settings
    src_dir = args.src_dir
    root_dst_dir = args.root_dst_dir
    make_dir(root_dst_dir)
    format_list = [".mp4", ".mov"]
    interval = args.interval

    # make dirs
    dst_dir = os.path.join(root_dst_dir, src_dir.split("/")[-1])
    make_dir(dst_dir)
    video_path_list = []
    listdir(src_dir, video_path_list, [".mov", ".mp4"])
    random.shuffle(video_path_list)
    # spilt the list for muti-processes
    processes_num = 8
    son_list = split_list(video_path_list, processes_num)
    print("sum of son process: {}".format(len(son_list)))
    print("average lenth in son process: {}".format(len(video_path_list)//processes_num))

    def process_operate(input_list):
        face_detector = detector_mtcnn(torch.device("cuda:{}".format(args.gpu)))
        video_num = len(input_list)
        for video_n, video_path in enumerate(input_list):
            image_dir = video_path
            for fmt in format_list:
                image_dir = image_dir.rstrip(fmt)
            video_name = os.path.join(image_dir.split("/")[-2], image_dir.split("/")[-1])
            image_dir = os.path.join(dst_dir, video_name)
            make_dir(image_dir)

            # read video and txt
            videoCapture = cv2.VideoCapture(video_path)

            frame_n = 0
            save_n = 0
            while True:
                # for SiW prot.1
                if save_n >= 60:
                    break
                success,frame = videoCapture.read()
                if not success:
                    break
                if(frame_n%interval == 0):
                    image_path = os.path.join(image_dir, "{}_{}.jpg".format(video_name.split("/")[-1], save_n))
                    if os.path.exists(image_path):
                        frame_n += 1
                        save_n += 1
                        print("pass")
                        continue
                    # save frame
                    cv2.imwrite(image_path, frame)
                    print("[{}/{}]saving {}".format(video_n+1, video_num, image_path))
                    # save dat
                    dat_path = os.path.join(image_dir, "{}_{}.dat".format(video_name.split("/")[-1], save_n))
                    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                    save_n = save_n+1
                    try:
                        bounding_boxes, landmarks = face_detector.detect_faces(img)
                        list(bounding_boxes).sort(key=sort_help, reverse=True)
                        # return [x1, y1, x2, y2]
                        bounding_box = bounding_boxes[0]
                        w = int(bounding_box[2]-bounding_box[0])
                        h = int(bounding_box[3]-bounding_box[1])
                        x1 = int((bounding_box[0]+bounding_box[2])//2-0.5*w)
                        y1 = int((bounding_box[1]+bounding_box[3])//2-0.5*h)
                        record = [x1, y1, w, h]
                    except:
                        frame_n += 1
                        continue
                    with open(dat_path, 'w') as write_file:
                        for i in range(4):
                            write_file.write(str(record[i]))
                            write_file.write('\n')

                    print("[{}/{}]writing {}".format(video_n+1, video_num, dat_path))
                    
                frame_n += 1
    process_list = []
    for i in range(len(son_list)):
        p = Process(target=process_operate, args=(son_list[i],))
        process_list.append(p)
    for p in process_list:
        p.start()
    print("Sub-process all done.")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tranfer videos to images")
    parser.add_argument('--src_dir', type=str, default="./pack/demo", help="root dir of videos")
    parser.add_argument('--root_dst_dir', type=str, default="./oulu_images", help="root dst dir of images")
    parser.add_argument('--gpu', type=str, default="6", help="set gpu num")
    parser.add_argument('--interval', type=int, default=1, help="split interval")
    args = parser.parse_args()
    main(args)