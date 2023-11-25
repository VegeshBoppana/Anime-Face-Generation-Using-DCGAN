#importing the modules
import os
import numpy as np
import matplotlib.pyplot as plt
import warnings
from tqdm.notebook import tqdm

from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img , array_to_img
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy

warnings.filterwarnings('ignore')


#LOAD FILES

BASE_DIR = "D:\Anime-Face-Generation-Using-DCGAN\data"

image_paths = []
for image_name in os.listdir(BASE_DIR):
    image_path = os.path.join(BASE_DIR, image_name)
    image_paths.append(image_path)

# print(image_paths[:5])





