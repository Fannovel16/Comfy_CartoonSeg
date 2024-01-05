# Copyright (c) OpenMMLab. All rights reserved.
from custom_mmengine_0102.config import read_base
from custom_mmengine_0102.runner.loops import EpochBasedTrainLoop

with read_base():
    from .dino_4scale_r50_8xb2_12e_coco import *

max_epochs = 36
train_cfg.update(
    dict(type=EpochBasedTrainLoop, max_epochs=max_epochs, val_interval=1))

param_scheduler[0].update(dict(milestones=[30]))
