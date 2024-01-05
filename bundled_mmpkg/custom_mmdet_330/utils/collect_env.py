# Copyright (c) OpenMMLab. All rights reserved.
from custom_mmengine_0102.utils import get_git_hash
from custom_mmengine_0102.utils.dl_utils import collect_env as collect_base_env

import custom_mmdet_330 as mmdet


def collect_env():
    """Collect the information of the running environments."""
    env_info = collect_base_env()
    env_info['MMDetection'] = mmdet.__version__ + '+' + get_git_hash()[:7]
    return env_info


if __name__ == '__main__':
    for name, val in collect_env().items():
        print(f'{name}: {val}')
