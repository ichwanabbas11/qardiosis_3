from flask import Flask

import h5py, skimage, matplotlib, scipy, tqdm, pickle
import pprint
import shutil
import re
import errno
import itertools
import sklearn, xgboost
import tensorflow as tf
import nibabel as nib
import numpy as np
import pandas as pd
import pandas as pd
import SimpleITK as sp

print("SimpleITK==", sp.__version__)
print("pandas==", pd.__version__)
print("numpy==", np.__version__)
print("nibabel==", nib.__version__)
print("tensorflow==", tf.__version__)
print("tqdm==",tqdm.__version__)
print("xgboost==",xgboost.__version__)
print("sklearn==",sklearn.__version__)
print("re==",re.__version__)
print("h5py==",h5py.__version__)
print("skimage==",skimage.__version__)
print("matplotlib==",matplotlib.__version__)
print("scipy==",scipy.__version__)