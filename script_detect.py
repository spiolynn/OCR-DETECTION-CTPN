# -*- coding: utf-8 -*-
"""
@author: limingfan
模型将被训练和验证。 验证结果将存储在./data_valid/results中。
ckpt文件将存储在新建的目录./model_detect中。
"""

import model_detect_meta as meta
import model_detect_data as model_data
from model_detect_wrap import ModelDetect


import os
#
os.environ['CUDA_VISIBLE_DEVICES'] = '1' #使用 GPU 0
#os.environ['CUDA_VISIBLE_DEVICES'] = '0,1' # 使用 GPU 0，1
#


#
model = ModelDetect()
#



# data
print('loading data ...')
data_train = model_data.get_files_with_ext(meta.dir_images_train, 'png')
data_valid = model_data.get_files_with_ext(meta.dir_images_valid, 'png')
print('load finished.')

#
# train
model.train_and_valid(data_train, data_valid)
#


#
# predict
model.prepare_for_prediction()
#
list_images_valid = model_data.get_files_with_ext(meta.dir_images_valid, 'png')
for img_file in list_images_valid:
    #
    # img_file = './data_test/images/bkgd_1_0_generated_0.png'
    #
    print(img_file)
    #
    conn_bbox, text_bbox, conf_bbox = model.predict(img_file, out_dir = './results_prediction')
    #

