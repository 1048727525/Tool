# 对于训练集需要保证：活体图片存在对应的深度图，非活体则不做要求
# 对于测试集，因为测试分数的缘故，需要保证活体与非活体均存在深度图


import os
from glob import glob
import cv2
import shutil




def oulu_op():
    type_data = "Dev_files"
    dst_path = os.path.join("oulu_images_crop", type_data)
    depth_path = os.path.join("oulu_images_crop/Depth", type_data)
    #img_path = "oulu_images_crop/"
    video_name_list = os.listdir(dst_path)
    for video_name in video_name_list:
        txt_writer = open(os.path.join(dst_path, video_name, "{}.txt".format(video_name)), 'w')
        print("save {}".format(os.path.join(dst_path, video_name, "{}.txt".format(video_name))))
        if video_name.split("_")[-1]=="1":
            label = True
        else:
            label = False
        jpg_path_list = glob(os.path.join(os.path.join(dst_path, video_name), "*.jpg"))
        #glob(os.path.join(image_path, "*.jpg"))
        jpg_path_list.sort(key=lambda x:int(x.split("_")[-2]))
        for img_path in jpg_path_list:
            img_name = img_path.split("/")[-1]
            depth_path = img_path.replace("oulu_images_crop", "oulu_images_crop/Depth").replace("scene.jpg", "depth1D.jpg")
            if type_data=="Train_files":
                if label:
                    if os.path.exists(depth_path) and os.path.exists(img_path):
                        txt_writer.write("{}\n".format(img_name))
                else:
                    if os.path.exists(img_path):
                        txt_writer.write("{}\n".format(img_name))
            else:
                if os.path.exists(depth_path) and os.path.exists(img_path):
                    txt_writer.write("{}\n".format(img_name))
        txt_writer.close()

def casia_mfsd_op():
    type_data = "test_release"
    dst_path = os.path.join("img_CASIA_FASD", type_data)
    depth_path = os.path.join("img_CASIA_FASD/depth", type_data)
    person_list = os.listdir(dst_path)
    for person_name in person_list:
        video_name_list = os.listdir(os.path.join(dst_path, person_name))
        for video_name in video_name_list:
            txt_writer = open(os.path.join(dst_path, person_name, video_name, "{}.txt".format(video_name)), 'w')
            print("save {}".format(os.path.join(dst_path, person_name, video_name, "{}.txt".format(video_name))))

            jpg_path_list = glob(os.path.join(os.path.join(dst_path, person_name, video_name), "*.jpg"))
            jpg_path_list.sort(key=lambda x:int(x.rstrip(".jpg").split("_")[-1]))
            for img_path in jpg_path_list:
                img_name = img_path.split("/")[-1]
                depth_path = img_path.replace("img_CASIA_FASD", "img_CASIA_FASD/depth").replace(".jpg", "_depth.jpg")
                map_x = cv2.imread(depth_path)
                if os.path.exists(depth_path) and (map_x is None):
                    os.remove(depth_path)
                if os.path.exists(depth_path) and os.path.exists(img_path) and not(map_x is None):
                    txt_writer.write("{}\n".format(img_name))
            txt_writer.close()

def MSU_MFSD_op():
    type_data_list = ["attack", "real"]
    for type_data in type_data_list:
        dst_path = os.path.join("img_MSU_MFSD", type_data)
        depth_path = os.path.join("img_MSU_MFSD/depth", type_data)
        video_list = os.listdir(dst_path)
        for video_name in video_list:
            txt_writer = open(os.path.join(dst_path, video_name, "{}.txt".format(video_name)), 'w')
            print("save {}".format(os.path.join(dst_path, video_name, "{}.txt".format(video_name))))

            jpg_path_list = glob(os.path.join(os.path.join(dst_path, video_name), "*.jpg"))
            jpg_path_list.sort(key=lambda x:int(x.rstrip(".jpg").split("_")[-1]))

            for img_path in jpg_path_list:
                img_name = img_path.split("/")[-1]
                depth_path = img_path.replace("img_MSU_MFSD", "img_MSU_MFSD/depth").replace(".jpg", "_depth.jpg")
                map_x = cv2.imread(depth_path)
                if os.path.exists(depth_path) and (map_x is None):
                    os.remove(depth_path)
                if os.path.exists(depth_path) and os.path.exists(img_path) and not(map_x is None):
                    txt_writer.write("{}\n".format(img_name))
        txt_writer.close()

            


def replayattack_op():
    type_data_list = ["devel", "test", "train"]
    for type_data in type_data_list:
        dst_path = os.path.join("img_replayattack", type_data)
        depth_path = os.path.join("img_replayattack/depth", type_data)
        video_type_list = os.listdir(dst_path)
        for video_type in video_type_list:
            if video_type=="attack":
                place_type_list = os.listdir(os.path.join(os.path.join(dst_path, video_type)))
                for place_type in place_type_list:
                    video_name_list = os.listdir(os.path.join(os.path.join(dst_path, video_type, place_type)))
                    for video_name in video_name_list:
                        txt_writer = open(os.path.join(dst_path, video_type, place_type, video_name, "{}.txt".format(video_name)), 'w')
                        print("save {}".format(os.path.join(dst_path, video_type, place_type, video_name, "{}.txt".format(video_name))))

                        jpg_path_list = glob(os.path.join(os.path.join(dst_path, video_type, place_type, video_name), "*.jpg"))
                        jpg_path_list.sort(key=lambda x:int(x.rstrip(".jpg").split("_")[-1]))
                        for img_path in jpg_path_list:
                            img_name = img_path.split("/")[-1]
                            depth_path = img_path.replace("img_replayattack", "img_replayattack/depth").replace(".jpg", "_depth.jpg")
                            if os.path.exists(depth_path) and os.path.exists(img_path):
                                txt_writer.write("{}\n".format(img_name))
                        txt_writer.close()
            else:
                video_name_list = os.listdir(os.path.join(os.path.join(dst_path, video_type)))
                for video_name in video_name_list:
                    txt_writer = open(os.path.join(dst_path, video_type, video_name, "{}.txt".format(video_name)), 'w')
                    print("save {}".format(os.path.join(dst_path, video_type, video_name, "{}.txt".format(video_name))))

                    jpg_path_list = glob(os.path.join(os.path.join(dst_path, video_type, video_name), "*.jpg"))
                    jpg_path_list.sort(key=lambda x:int(x.rstrip(".jpg").split("_")[-1]))
                    for img_path in jpg_path_list:
                        img_name = img_path.split("/")[-1]
                        depth_path = img_path.replace("img_replayattack", "img_replayattack/depth").replace(".jpg", "_depth.jpg")
                        if os.path.exists(depth_path) and os.path.exists(img_path):
                            txt_writer.write("{}\n".format(img_name))
                    txt_writer.close()

def SiW_op():
    type_data_list = ["Test", "Train", "Train_60"]
    for type_data in type_data_list:
        dst_path = os.path.join("SiW_images_crop", type_data)
        depth_path = os.path.join("SiW_images_crop/Depth", type_data)
        video_type_list = os.listdir(dst_path)
        for video_type in video_type_list:
            people_list = os.listdir(os.path.join(dst_path, video_type))
            for people_num in people_list:
                video_name_list = os.listdir(os.path.join(dst_path, video_type, people_num))
                for video_name in video_name_list:
                    video_path = os.path.join(dst_path, video_type, people_num, video_name)
                    txt_writer = open(os.path.join(dst_path, video_type, people_num, video_name, "{}.txt".format(video_name)), 'w')
                    print("save {}".format(os.path.join(dst_path, video_type, people_num, video_name, "{}.txt".format(video_name))))
                    jpg_path_list = glob(os.path.join(os.path.join(dst_path, video_type, people_num, video_name), "*.jpg"))
                    jpg_path_list.sort(key=lambda x:int(x.rstrip(".jpg").split("_")[-1]))
                    for img_path in jpg_path_list:
                        img_name = img_path.split("/")[-1]
                        depth_path = img_path.replace("SiW_images_crop", "SiW_images_crop/Depth").replace(".jpg", "_depth.jpg")
                        if video_type == "live":
                            if os.path.exists(depth_path) and os.path.exists(img_path):
                                txt_writer.write("{}\n".format(img_name))
                        elif video_type == "spoof":
                            if os.path.exists(img_path):
                                txt_writer.write("{}\n".format(img_name))
                    txt_writer.close()

def SiW_op_2():
    src_txt_path = "SiW_images_crop/Protocols/Protocol_1/Train.txt"
    dst_txt_path = "SiW_images_crop/Protocols/SiW.txt"
    with open(src_txt_path, 'r') as file_read:
        lines = file_read.readlines()
    with open(dst_txt_path, 'w') as file_write:
        for line in lines:
            file_write.write(line.replace("Train_60", "Train"))

def listdir(path, list_name, type_list):
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name, type_list) 
        elif os.path.splitext(file_path)[1] in type_list:  
            list_name.append(file_path)

def SiW_train_1_help():
    src_path = "oulu_images_crop/Train_files"
    txt_path_list = []
    listdir(src_path, txt_path_list, [".txt"])
    for txt_path in txt_path_list:
        with open(txt_path, 'r') as read_file:
            lines = read_file.readlines()
        if len(lines)<40:
            res = []
            while True:
                if len(res)<40:
                    res+=lines
                else:
                    break
            with open(txt_path, 'w') as write_file:
                write_file.writelines(res)
                print(txt_path)

def oulu_op():
    type_data_list = ["Dev_files", "Test_files", "Train_files"]
    for type_data in type_data_list:
        if type_data=="Train_files":
            dev_set = os.listdir("oulu_images_crop/Train_files")
            with open("oulu_images_crop/train_list_video.txt", 'w') as f_writer:
                for name in dev_set:
                    print(name)
                    if name.split("_")[-1]=="1":
                        f_writer.write("+1,{}\n".format(name))
                    else:
                        f_writer.write("-1,{}\n".format(name))

def oulu_op_2():
    txt_list = ["oulu_images_crop/train_list_video.txt", "oulu_images_crop/dev_list_video.txt", "oulu_images_crop/test_list_video.txt"]
    with open("oulu_images_crop/oulu.txt", 'w') as f_writer:
        for txt_path in txt_list:
            with open(txt_path, 'r') as f_reader:
                lines = f_reader.readlines()
            f_writer.writelines(lines)


def oulu_op_3():
    root_dir = "oulu_images_crop"
    type_data_list = ["Dev_files", "Test_files", "Train_files"]
    for type_data in type_data_list:
        video_set = os.listdir(os.path.join(root_dir, type_data))
        img_dir = os.path.join("oulu_images_crop", type_data)
        depth_dir = os.path.join("oulu_images_crop/Depth", type_data)
        for video_name in video_set:
            txt_path = os.path.join(root_dir, type_data, video_name, "{}.txt".format(video_name))
            dst_txt_path = os.path.join(root_dir, type_data, video_name, "{}_cross.txt".format(video_name))
            print(dst_txt_path)
            if type_data=="Train_files":
                print(video_name)
                with open(txt_path, 'r') as f_reader:
                    lines = f_reader.readlines()
                    lines_write = []
                    for line in lines:
                        img_name = line.strip()
                        depth_name = img_name.replace("scene", "depth1D")
                        img_path = os.path.join(img_dir, img_name)
                        depth_path = os.path.join(depth_dir, depth_name)
                        if os.path.exists(depth_path) and os.path.exists(img_path):
                            lines_write.append(line)
                if os.path.exists(dst_txt_path):
                    os.remove(dst_txt_path)
                # with open(dst_txt_path, 'w') as f_writer:
                #     f_writer.writelines(lines_write)

def oulu_op_4():
    txt_list = ["oulu_images_crop/test_list_video.txt", "oulu_images_crop/dev_list_video.txt"]
    with open("oulu_images_crop/test_dev_list_video.txt", 'w') as f_writer:
        for txt_path in txt_list:
            with open(txt_path, 'r') as f_reader:
                lines = f_reader.readlines()
            f_writer.writelines(lines)
            



if __name__ == '__main__':
    oulu_op_4()
