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
    Train_live_list = []
    listdir("Train/live", Train_live_list, [".mov"])
    with open("Protocols/Protocols_3/Train_2.txt", 'w') as f:
        for name in Train_live_list:
            line = "+1,{}\n".format(name.replace(".mov", "").replace(".m", ""))
            f.write(line)

    Train_spoof_list = []
    listdir("Train/spoof", Train_spoof_list, [".mov"])
    with open("Protocols/Protocols_3/Train_2.txt", 'a') as f:
        for name in Train_spoof_list:
            name = name.replace(".mov", "").replace(".m", "")
            if name.split("-")[-3]=="2":
                line = "-1,{}\n".format(name)
                f.write(line)

    Test_live_list = []
    listdir("Test/live", Test_live_list, [".mov"])
    with open("Protocols/Protocols_3/Test_2.txt", 'w') as f:
        for name in Test_live_list:
            line = "+1,{}\n".format(name.replace(".mov", "").replace(".m", ""))
            f.write(line)

    Test_spoof_list = []
    listdir("Test/spoof", Test_spoof_list, [".mov"])
    with open("Protocols/Protocols_3/Test_2.txt", 'a') as f:
        for name in Test_spoof_list:
            name = name.replace(".mov", "").replace(".m", "")
            if name.split("-")[-3]=="3":
                line = "-1,{}\n".format(name)
                f.write(line)




    '''
    help_list = []
    with open("Protocols/Protocols_1/Train.txt", 'r') as f:
        help_list = f.readlines()
    with open("Protocols/Protocols_1/Train.txt", "w") as f:
        for line in help_list:
            line = line.replace("Train", "Train_60")
            f.write(line)
    '''
