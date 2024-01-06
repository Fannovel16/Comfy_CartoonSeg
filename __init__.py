import sys, os
from pathlib import Path
#Ref: https://github.com/comfyanonymous/ComfyUI/blob/76d53c4622fc06372975ed2a43ad345935b8a551/nodes.py#L17
here = Path(__file__).parent.resolve()
sys.path.insert(0, str(Path(here, "src").resolve()))