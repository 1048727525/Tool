# for oulu
#nohup python -u main.py --src_dir /ssd1/wangzhuo/data/oulu_npu/oulu_images/Dev_files/ --gpu 7 > op_oulu_dev.log 2>&1 &
#nohup python -u main.py --src_dir /ssd1/wangzhuo/data/oulu_npu/oulu_images/Test_files/ --gpu 2 > op_oulu_test.log 2>&1 &
#nohup python -u main.py --src_dir /ssd1/wangzhuo/data/oulu_npu/oulu_images/Train_files/ --gpu 1 > op_oulu_train.log 2>&1 &

# for casia
#nohup python -u main.py --src_dir /ssd1/wangzhuo/data/img_CASIA_FASD/test_release/ --gpu 2 > op_cf_test.log 2>&1 &
#nohup python -u main.py --src_dir /ssd1/wangzhuo/data/img_CASIA_FASD/train_release/ --gpu 2 > op_cf_train.log 2>&1 &

# for replayattack
nohup python -u main.py --src_dir /ssd1/wangzhuo/data/img_replayattack/devel/ --gpu 2 > op_ra_devel.log 2>&1 &
nohup python -u main.py --src_dir /ssd1/wangzhuo/data/img_replayattack/test/ --gpu 3 > op_ra_test.log 2>&1 &
nohup python -u main.py --src_dir /ssd1/wangzhuo/data/img_replayattack/train/ --gpu 3 > op_ra_train.log 2>&1 &