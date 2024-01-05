# Copyright (c) OpenMMLab. All rights reserved.
from custom_mmengine_0102.config import read_base
from custom_mmengine_0102.model.weight_init import PretrainedInit

with read_base():
    from .detr_r50_8xb2_500e_coco import *

model.update(
    dict(
        backbone=dict(
            depth=101,
            init_cfg=dict(
                type=PretrainedInit, checkpoint='torchvision://resnet101'))))
