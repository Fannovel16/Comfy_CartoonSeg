# Copyright (c) OpenMMLab. All rights reserved.

# Please refer to https://mmengine.readthedocs.io/en/latest/advanced_tutorials/config.html#a-pure-python-style-configuration-file-beta for more details. # noqa
# mmcv >= 2.0.1
# mmengine >= 0.8.0

from custom_mmengine_0102.config import read_base

with read_base():
    from .mask_rcnn_r50_fpn_2x_coco import *

from custom_mmengine_0102.model.weight_init import PretrainedInit

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(
            type=PretrainedInit, checkpoint='torchvision://resnet101')))
