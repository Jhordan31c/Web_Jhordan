import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR,'Web_Jhordan/static')

print(STATIC_ROOT)