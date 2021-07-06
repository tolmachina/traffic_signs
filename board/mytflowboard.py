from datetime import datetime
import io
import itertools
from packaging import version

import tensorflow as tf
from tensorflow import keras

import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics
import pathlib
import PIL
import PIL.Image

import cv2

BATCH_SIZE = 32
img_height = 30
img_width = 30
data_dir = "/Volumes/Seagate/Databases/gtsrb/"

img_dir = pathlib.Path(data_dir)
image_count = len(list(img_dir.glob('*/*.ppm')))
print("Image_count", image_count)



img = np.reshape(train_images[0], (-1, 28, 28, 1))

logdir = "logs/train_data/" + datetime.now().strftime("%Y%m%d-%H%M%S")
# Creates a file writer for the log directory.
file_writer = tf.summary.create_file_writer(logdir)

# Using the file writer, log the reshaped image.
with file_writer.as_default():
  tf.summary.image("Training data", img, step=0)


class_names = train_ds.class_names
print(class_names)
