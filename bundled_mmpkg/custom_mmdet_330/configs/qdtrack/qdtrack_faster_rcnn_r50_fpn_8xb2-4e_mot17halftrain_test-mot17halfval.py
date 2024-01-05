# Copyright (c) OpenMMLab. All rights reserved.
from custom_mmengine_0102.config import read_base

with read_base():
    from .._base_.datasets.mot_challenge import *
    from .qdtrack_faster_rcnn_r50_fpn_4e_base import *

from custom_mmdet_330.evaluation import CocoVideoMetric, MOTChallengeMetric

# evaluator
val_evaluator = [
    dict(type=CocoVideoMetric, metric=['bbox'], classwise=True),
    dict(type=MOTChallengeMetric, metric=['HOTA', 'CLEAR', 'Identity'])
]
