from mmengine import Config
db_config = Config.fromfile('/home/yunkr/github/mmocr/configs/textdet/dbnet/dbnet_resnet18_fpnc_1200e_icdar2015.py')

for i, item in enumerate(db_config):
    print(f"{i}\t{item}\t{db_config[item]}\n")

