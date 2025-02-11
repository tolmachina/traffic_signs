import cv2
import numpy as np
import os
import sys
import tensorflow as tf
from datetime import datetime
from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4

# path to data for second argument of program run 
# 
# /Volumes/Seagate/Databases/gtsrb
def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])
    
    # converting vector of integer to binary class matrix
    labels = tf.keras.utils.to_categorical(labels)
    
    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network. THE MODEL
    model = get_model()

    # create logs FIT directory
    log_dir = "logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")

    # a callback for datetime directory
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS,validation_data=(x_test, y_test), callbacks=[tensorboard_callback])

    # # Evaluate neural network performance
    print("start evaluation on test data...")
    model.evaluate(x_test, y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")

    # predictions
    predictions = model.predict(x_test, verbose=1)
    for i in range(10):
        print("Prediction guess =", np.argmax(predictions[i]),"    probabality = ", max(predictions[i]))
        print("Label   category =", np.argmax(y_test[i]))


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. 
    
    `images` should be a list of all of the images in the data directory, 
    where each image is formatted as a numpy ndarray with 
    dimensions IMG_WIDTH x IMG_HEIGHT x 3. 
    
    `labels` should be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    images = []
    labels = []
    for dir in os.listdir(data_dir):
        # get path and filename
        if dir[0] != ".":
            path = os.path.join(data_dir, dir)
            category = path.split(os.sep)[-1:]
            filename = os.listdir(path)
    
            # get img and scale it to 30,30
            for fname in filename:
                filepath = os.path.join(path,fname)
                img = cv2.imread(filepath)
                if img is None:
                    sys.exit("Could not read the image.")
                res = cv2.resize(img,(IMG_HEIGHT,IMG_WIDTH),interpolation = cv2.INTER_AREA)
                
                # add to image list and category list
                images.append(res)
                labels.append(int(category[0]))
                
    return (images,labels)

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(
        16,(3,3),activation="relu",input_shape=(IMG_WIDTH,IMG_HEIGHT,3)
    ))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
    model.add(tf.keras.layers.Conv2D(64,(3,3),activation = "relu"))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(256, activation="relu"))
    model.add(tf.keras.layers.Dense(512, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax"))
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    model.summary()
    return model


if __name__ == "__main__":
    main()