import glob
import os
import shutil
import json

try:
   os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")