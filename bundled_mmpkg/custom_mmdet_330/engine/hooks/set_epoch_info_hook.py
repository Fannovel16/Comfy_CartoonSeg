# Copyright (c) OpenMMLab. All rights reserved.
from custom_mmengine_0102.hooks import Hook
from custom_mmengine_0102.model.wrappers import is_model_wrapper

from custom_mmdet_330.registry import HOOKS


@HOOKS.register_module()
class SetEpochInfoHook(Hook):
    """Set runner's epoch information to the model."""

    def before_train_epoch(self, runner):
        epoch = runner.epoch
        model = runner.model
        if is_model_wrapper(model):
            model = model.module
        model.set_epoch(epoch)
