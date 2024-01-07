#Thanks @ltdrdata
#https://github.com/ltdrdata/ComfyUI-Impact-Pack/blob/f6ec3a8164773a4e246bc564803672b63cc52e59/install.py
import sys
import platform
import subprocess
import threading
import locale
import os

def handle_stream(stream, is_stdout):
    stream.reconfigure(encoding=locale.getpreferredencoding(), errors='replace')

    for msg in stream:
        if is_stdout:
            print(msg, end="", file=sys.stdout)
        else: 
            print(msg, end="", file=sys.stderr)

def process_wrap(cmd_str, cwd=None, handler=None):
    print(f"[Comfy-CartoonSeg] EXECUTE: {cmd_str} in '{cwd}'")
    process = subprocess.Popen(cmd_str, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

    if handler is None:
        handler = handle_stream

    stdout_thread = threading.Thread(target=handler, args=(process.stdout, True))
    stderr_thread = threading.Thread(target=handler, args=(process.stderr, False))

    stdout_thread.start()
    stderr_thread.start()

    stdout_thread.join()
    stderr_thread.join()

    return process.wait()

if "python_embeded" in sys.executable or "python_embedded" in sys.executable:
    pip_install = [sys.executable, '-s', '-m', 'pip', 'install']
    mim_install = [sys.executable, '-s', '-m', 'mim', 'install']
else:
    pip_install = [sys.executable, '-m', 'pip', 'install']
    mim_install = [sys.executable, '-m', 'mim', 'install']

process_wrap(pip_install + ['openmim'])
try:
    import pycocotools
except Exception:
    if platform.system() not in ["Windows"] or platform.machine() not in ["AMD64", "x86_64"]:
        print(f"Your system is {platform.system()}; !! You need to install 'libpython3-dev' for this step. !!")

        process_wrap(pip_install + ['pycocotools'])
    else:
        pycocotools = {
            (3, 8): "https://github.com/Bing-su/dddetailer/releases/download/pycocotools/pycocotools-2.0.6-cp38-cp38-win_amd64.whl",
            (3, 9): "https://github.com/Bing-su/dddetailer/releases/download/pycocotools/pycocotools-2.0.6-cp39-cp39-win_amd64.whl",
            (3, 10): "https://github.com/Bing-su/dddetailer/releases/download/pycocotools/pycocotools-2.0.6-cp310-cp310-win_amd64.whl",
            (3, 11): "https://github.com/Bing-su/dddetailer/releases/download/pycocotools/pycocotools-2.0.6-cp311-cp311-win_amd64.whl",
        }

        version = sys.version_info[:2]
        url = pycocotools[version]
        process_wrap(pip_install + [url])

def ensure_mmdet_package():
    try:
        import mmcv
        import mmdet
        from mmdet.evaluation import get_classes
    except Exception:
        process_wrap(pip_install + ['opendatalab==0.0.9'])
        process_wrap(pip_install + ['-U', 'openmim'])
        process_wrap(mim_install + ['mmdet==3.3.0'])

my_path = os.path.dirname(__file__)
requirements_path = os.path.join(my_path, "other_requirements.txt")
ensure_mmdet_package()
process_wrap(pip_install + ['-r', requirements_path])