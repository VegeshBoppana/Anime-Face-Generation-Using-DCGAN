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
# print(len(image_paths))

#                VISUALIZE THE IMAGE DATA SET TO DISPLAY GIRD OF IMAGES

plt.figure(figsize =(20, 20))
temp_images = image_paths[:49]
index = 1

for image_path in temp_images:
    plt.subplot(7 , 7 , index)

    img = load_img(image_path)

    img = np.array(img)
    plt.imshow(img)
    plt.axis('off') # in colab or jupyter notebooks convert this line of code as "  plt.axis('/off) "
    index+=1


#prep process the images
train_images = [np.array(load_img(path)) for path in tqdm(image_paths)]
train_images = np.array(train_images)










