#nohup python -u crop_img.py --src_root_dir ./Test/live --dst_root_dir ../SiW_images_crop > crop_siw_test_live.log 2>&1 &
#nohup python -u crop_img.py --src_root_dir ./Test/spoof --dst_root_dir ../SiW_images_crop > crop_siw_test_spoof.log 2>&1 &
#nohup python -u crop_img.py --src_root_dir ./Train/live --dst_root_dir ../SiW_images_crop > crop_siw_train_live.log 2>&1 &
#nohup python -u crop_img.py --src_root_dir ./Train/spoof --dst_root_dir ../SiW_images_crop > crop_siw_train_spoof.log 2>&1 &
nohup python -u crop_img.py --src_root_dir ./Train_60/spoof --dst_root_dir ../SiW_images_crop > crop_siw_train_spoof.log 2>&1 &
nohup python -u crop_img.py --src_root_dir ./Train_60/live --dst_root_dir ../SiW_images_crop > crop_siw_train_live.log 2>&1 &