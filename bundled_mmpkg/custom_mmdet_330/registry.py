# Copyright (c) OpenMMLab. All rights reserved.
"""MMDetection provides 17 registry nodes to support using modules across
projects. Each node is a child of the root registry in MMEngine.

More details can be found at
https://mmengine.readthedocs.io/en/latest/tutorials/registry.html.
"""

from custom_mmengine_0102.registry import DATA_SAMPLERS as MMENGINE_DATA_SAMPLERS
from custom_mmengine_0102.registry import DATASETS as MMENGINE_DATASETS
from custom_mmengine_0102.registry import EVALUATOR as MMENGINE_EVALUATOR
from custom_mmengine_0102.registry import HOOKS as MMENGINE_HOOKS
from custom_mmengine_0102.registry import LOG_PROCESSORS as MMENGINE_LOG_PROCESSORS
from custom_mmengine_0102.registry import LOOPS as MMENGINE_LOOPS
from custom_mmengine_0102.registry import METRICS as MMENGINE_METRICS
from custom_mmengine_0102.registry import MODEL_WRAPPERS as MMENGINE_MODEL_WRAPPERS
from custom_mmengine_0102.registry import MODELS as MMENGINE_MODELS
from custom_mmengine_0102.registry import \
    OPTIM_WRAPPER_CONSTRUCTORS as MMENGINE_OPTIM_WRAPPER_CONSTRUCTORS
from custom_mmengine_0102.registry import OPTIM_WRAPPERS as MMENGINE_OPTIM_WRAPPERS
from custom_mmengine_0102.registry import OPTIMIZERS as MMENGINE_OPTIMIZERS
from custom_mmengine_0102.registry import PARAM_SCHEDULERS as MMENGINE_PARAM_SCHEDULERS
from custom_mmengine_0102.registry import \
    RUNNER_CONSTRUCTORS as MMENGINE_RUNNER_CONSTRUCTORS
from custom_mmengine_0102.registry import RUNNERS as MMENGINE_RUNNERS
from custom_mmengine_0102.registry import TASK_UTILS as MMENGINE_TASK_UTILS
from custom_mmengine_0102.registry import TRANSFORMS as MMENGINE_TRANSFORMS
from custom_mmengine_0102.registry import VISBACKENDS as MMENGINE_VISBACKENDS
from custom_mmengine_0102.registry import VISUALIZERS as MMENGINE_VISUALIZERS
from custom_mmengine_0102.registry import \
    WEIGHT_INITIALIZERS as MMENGINE_WEIGHT_INITIALIZERS
from custom_mmengine_0102.registry import Registry

# manage all kinds of runners like `EpochBasedRunner` and `IterBasedRunner`
RUNNERS = Registry(
    'runner', parent=MMENGINE_RUNNERS, locations=['mmdet.engine.runner'])
# manage runner constructors that define how to initialize runners
RUNNER_CONSTRUCTORS = Registry(
    'runner constructor',
    parent=MMENGINE_RUNNER_CONSTRUCTORS,
    locations=['mmdet.engine.runner'])
# manage all kinds of loops like `EpochBasedTrainLoop`
LOOPS = Registry(
    'loop', parent=MMENGINE_LOOPS, locations=['mmdet.engine.runner'])
# manage all kinds of hooks like `CheckpointHook`
HOOKS = Registry(
    'hook', parent=MMENGINE_HOOKS, locations=['mmdet.engine.hooks'])

# manage data-related modules
DATASETS = Registry(
    'dataset', parent=MMENGINE_DATASETS, locations=['mmdet.datasets'])
DATA_SAMPLERS = Registry(
    'data sampler',
    parent=MMENGINE_DATA_SAMPLERS,
    locations=['mmdet.datasets.samplers'])
TRANSFORMS = Registry(
    'transform',
    parent=MMENGINE_TRANSFORMS,
    locations=['mmdet.datasets.transforms'])

# manage all kinds of modules inheriting `nn.Module`
MODELS = Registry('model', parent=MMENGINE_MODELS, locations=['mmdet.models'])
# manage all kinds of model wrappers like 'MMDistributedDataParallel'
MODEL_WRAPPERS = Registry(
    'model_wrapper',
    parent=MMENGINE_MODEL_WRAPPERS,
    locations=['mmdet.models'])
# manage all kinds of weight initialization modules like `Uniform`
WEIGHT_INITIALIZERS = Registry(
    'weight initializer',
    parent=MMENGINE_WEIGHT_INITIALIZERS,
    locations=['mmdet.models'])

# manage all kinds of optimizers like `SGD` and `Adam`
OPTIMIZERS = Registry(
    'optimizer',
    parent=MMENGINE_OPTIMIZERS,
    locations=['mmdet.engine.optimizers'])
# manage optimizer wrapper
OPTIM_WRAPPERS = Registry(
    'optim_wrapper',
    parent=MMENGINE_OPTIM_WRAPPERS,
    locations=['mmdet.engine.optimizers'])
# manage constructors that customize the optimization hyperparameters.
OPTIM_WRAPPER_CONSTRUCTORS = Registry(
    'optimizer constructor',
    parent=MMENGINE_OPTIM_WRAPPER_CONSTRUCTORS,
    locations=['mmdet.engine.optimizers'])
# manage all kinds of parameter schedulers like `MultiStepLR`
PARAM_SCHEDULERS = Registry(
    'parameter scheduler',
    parent=MMENGINE_PARAM_SCHEDULERS,
    locations=['mmdet.engine.schedulers'])
# manage all kinds of metrics
METRICS = Registry(
    'metric', parent=MMENGINE_METRICS, locations=['mmdet.evaluation'])
# manage evaluator
EVALUATOR = Registry(
    'evaluator', parent=MMENGINE_EVALUATOR, locations=['mmdet.evaluation'])

# manage task-specific modules like anchor generators and box coders
TASK_UTILS = Registry(
    'task util', parent=MMENGINE_TASK_UTILS, locations=['mmdet.models'])

# manage visualizer
VISUALIZERS = Registry(
    'visualizer',
    parent=MMENGINE_VISUALIZERS,
    locations=['mmdet.visualization'])
# manage visualizer backend
VISBACKENDS = Registry(
    'vis_backend',
    parent=MMENGINE_VISBACKENDS,
    locations=['mmdet.visualization'])

# manage logprocessor
LOG_PROCESSORS = Registry(
    'log_processor',
    parent=MMENGINE_LOG_PROCESSORS,
    # TODO: update the location when mmdet has its own log processor
    locations=['mmdet.engine'])
