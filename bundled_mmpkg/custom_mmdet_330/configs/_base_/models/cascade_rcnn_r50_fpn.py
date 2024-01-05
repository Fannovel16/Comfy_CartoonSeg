# Copyright (c) OpenMMLab. All rights reserved.
from custom_mmcv_210.ops import RoIAlign, nms
from torch.nn import BatchNorm2d

from custom_mmdet_330.models.backbones.resnet import ResNet
from custom_mmdet_330.models.data_preprocessors.data_preprocessor import \
    DetDataPreprocessor
from custom_mmdet_330.models.dense_heads.rpn_head import RPNHead
from custom_mmdet_330.models.detectors.cascade_rcnn import CascadeRCNN
from custom_mmdet_330.models.losses.cross_entropy_loss import CrossEntropyLoss
from custom_mmdet_330.models.losses.smooth_l1_loss import SmoothL1Loss
from custom_mmdet_330.models.necks.fpn import FPN
from custom_mmdet_330.models.roi_heads.bbox_heads.convfc_bbox_head import \
    Shared2FCBBoxHead
from custom_mmdet_330.models.roi_heads.cascade_roi_head import CascadeRoIHead
from custom_mmdet_330.models.roi_heads.roi_extractors.single_level_roi_extractor import \
    SingleRoIExtractor
from custom_mmdet_330.models.task_modules.assigners.max_iou_assigner import MaxIoUAssigner
from custom_mmdet_330.models.task_modules.coders.delta_xywh_bbox_coder import \
    DeltaXYWHBBoxCoder
from custom_mmdet_330.models.task_modules.prior_generators.anchor_generator import \
    AnchorGenerator
from custom_mmdet_330.models.task_modules.samplers.random_sampler import RandomSampler

# model settings
model = dict(
    type=CascadeRCNN,
    data_preprocessor=dict(
        type=DetDataPreprocessor,
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        bgr_to_rgb=True,
        pad_size_divisor=32),
    backbone=dict(
        type=ResNet,
        depth=50,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type=BatchNorm2d, requires_grad=True),
        norm_eval=True,
        style='pytorch',
        init_cfg=dict(type='Pretrained', checkpoint='torchvision://resnet50')),
    neck=dict(
        type=FPN,
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        num_outs=5),
    rpn_head=dict(
        type=RPNHead,
        in_channels=256,
        feat_channels=256,
        anchor_generator=dict(
            type=AnchorGenerator,
            scales=[8],
            ratios=[0.5, 1.0, 2.0],
            strides=[4, 8, 16, 32, 64]),
        bbox_coder=dict(
            type=DeltaXYWHBBoxCoder,
            target_means=[.0, .0, .0, .0],
            target_stds=[1.0, 1.0, 1.0, 1.0]),
        loss_cls=dict(
            type=CrossEntropyLoss, use_sigmoid=True, loss_weight=1.0),
        loss_bbox=dict(type=SmoothL1Loss, beta=1.0 / 9.0, loss_weight=1.0)),
    roi_head=dict(
        type=CascadeRoIHead,
        num_stages=3,
        stage_loss_weights=[1, 0.5, 0.25],
        bbox_roi_extractor=dict(
            type=SingleRoIExtractor,
            roi_layer=dict(type=RoIAlign, output_size=7, sampling_ratio=0),
            out_channels=256,
            featmap_strides=[4, 8, 16, 32]),
        bbox_head=[
            dict(
                type=Shared2FCBBoxHead,
                in_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=80,
                bbox_coder=dict(
                    type=DeltaXYWHBBoxCoder,
                    target_means=[0., 0., 0., 0.],
                    target_stds=[0.1, 0.1, 0.2, 0.2]),
                reg_class_agnostic=True,
                loss_cls=dict(
                    type=CrossEntropyLoss, use_sigmoid=False, loss_weight=1.0),
                loss_bbox=dict(type=SmoothL1Loss, beta=1.0, loss_weight=1.0)),
            dict(
                type=Shared2FCBBoxHead,
                in_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=80,
                bbox_coder=dict(
                    type=DeltaXYWHBBoxCoder,
                    target_means=[0., 0., 0., 0.],
                    target_stds=[0.05, 0.05, 0.1, 0.1]),
                reg_class_agnostic=True,
                loss_cls=dict(
                    type=CrossEntropyLoss, use_sigmoid=False, loss_weight=1.0),
                loss_bbox=dict(type=SmoothL1Loss, beta=1.0, loss_weight=1.0)),
            dict(
                type=Shared2FCBBoxHead,
                in_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=80,
                bbox_coder=dict(
                    type=DeltaXYWHBBoxCoder,
                    target_means=[0., 0., 0., 0.],
                    target_stds=[0.033, 0.033, 0.067, 0.067]),
                reg_class_agnostic=True,
                loss_cls=dict(
                    type=CrossEntropyLoss, use_sigmoid=False, loss_weight=1.0),
                loss_bbox=dict(type=SmoothL1Loss, beta=1.0, loss_weight=1.0))
        ]),
    # model training and testing settings
    train_cfg=dict(
        rpn=dict(
            assigner=dict(
                type=MaxIoUAssigner,
                pos_iou_thr=0.7,
                neg_iou_thr=0.3,
                min_pos_iou=0.3,
                match_low_quality=True,
                ignore_iof_thr=-1),
            sampler=dict(
                type=RandomSampler,
                num=256,
                pos_fraction=0.5,
                neg_pos_ub=-1,
                add_gt_as_proposals=False),
            allowed_border=0,
            pos_weight=-1,
            debug=False),
        rpn_proposal=dict(
            nms_pre=2000,
            max_per_img=2000,
            nms=dict(type=nms, iou_threshold=0.7),
            min_bbox_size=0),
        rcnn=[
            dict(
                assigner=dict(
                    type=MaxIoUAssigner,
                    pos_iou_thr=0.5,
                    neg_iou_thr=0.5,
                    min_pos_iou=0.5,
                    match_low_quality=False,
                    ignore_iof_thr=-1),
                sampler=dict(
                    type=RandomSampler,
                    num=512,
                    pos_fraction=0.25,
                    neg_pos_ub=-1,
                    add_gt_as_proposals=True),
                pos_weight=-1,
                debug=False),
            dict(
                assigner=dict(
                    type=MaxIoUAssigner,
                    pos_iou_thr=0.6,
                    neg_iou_thr=0.6,
                    min_pos_iou=0.6,
                    match_low_quality=False,
                    ignore_iof_thr=-1),
                sampler=dict(
                    type=RandomSampler,
                    num=512,
                    pos_fraction=0.25,
                    neg_pos_ub=-1,
                    add_gt_as_proposals=True),
                pos_weight=-1,
                debug=False),
            dict(
                assigner=dict(
                    type=MaxIoUAssigner,
                    pos_iou_thr=0.7,
                    neg_iou_thr=0.7,
                    min_pos_iou=0.7,
                    match_low_quality=False,
                    ignore_iof_thr=-1),
                sampler=dict(
                    type=RandomSampler,
                    num=512,
                    pos_fraction=0.25,
                    neg_pos_ub=-1,
                    add_gt_as_proposals=True),
                pos_weight=-1,
                debug=False)
        ]),
    test_cfg=dict(
        rpn=dict(
            nms_pre=1000,
            max_per_img=1000,
            nms=dict(type=nms, iou_threshold=0.7),
            min_bbox_size=0),
        rcnn=dict(
            score_thr=0.05,
            nms=dict(type=nms, iou_threshold=0.5),
            max_per_img=100)))
