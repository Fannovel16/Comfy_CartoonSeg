# Copyright (c) OpenMMLab. All rights reserved.
from pathlib import Path
from typing import List

import custom_mmengine_0102 as mmengine
from custom_mmengine_0102.dataset import BaseDataset
from custom_mmengine_0102.fileio import get_file_backend

from custom_mmdet_330.registry import DATASETS


@DATASETS.register_module()
class CocoCaptionDataset(BaseDataset):
    """COCO2014 Caption dataset."""

    def load_data_list(self) -> List[dict]:
        """Load data list."""
        img_prefix = self.data_prefix['img_path']
        annotations = mmengine.load(self.ann_file)
        file_backend = get_file_backend(img_prefix)

        data_list = []
        for ann in annotations:
            data_info = {
                'img_id': Path(ann['image']).stem.split('_')[-1],
                'img_path': file_backend.join_path(img_prefix, ann['image']),
                'gt_caption': ann['caption'],
            }

            data_list.append(data_info)

        return data_list
