# MSU-MFSD
# nohup python -u video2img.py --src_dir ../MSU-MFSD/scene01/attack --root_dst_dir ../img_MSU_MFSD > op_attack.log 2>&1 &
# nohup python -u video2img.py --src_dir ../MSU-MFSD/scene01/real --root_dst_dir ../img_MSU_MFSD > op_real.log 2>&1 &

# SiW
#nohup python -u video2img.py --src_dir ../SiW_release/Test/live --root_dst_dir ../SiW_images/Test --interval 3 --gpu 6 > op_test_live.log 2>&1 &
# nohup python -u video2img.py --src_dir ../SiW_release/Test/spoof --root_dst_dir ../SiW_images/Test --interval 3 --gpu 7 > op_test_spoof.log 2>&1 &
# nohup python -u video2img.py --src_dir ../SiW_release/Train/live --root_dst_dir ../SiW_images/Train --interval 3 --gpu 5 > op_train_live.log 2>&1 &
# nohup python -u video2img.py --src_dir ../SiW_release/Train/spoof --root_dst_dir ../SiW_images/Train --interval 3 --gpu 4 > op_train_spoof.log 2>&1 &

# for SiW prot.1
nohup python -u video2img.py --src_dir ../SiW_release/Train/live --root_dst_dir ../SiW_images/Train_60 --interval 1 --gpu 6 > op_train_live.log 2>&1 &
nohup python -u video2img.py --src_dir ../SiW_release/Train/spoof --root_dst_dir ../SiW_images/Train_60 --interval 1 --gpu 7 > op_train_spoof.log 2>&1 &