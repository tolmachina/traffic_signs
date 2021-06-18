import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras
from traffic import load_data, EPOCHS, NUM_CATEGORIES, TEST_SIZE
from sklearn.model_selection import train_test_split

# Get image arrays and labels for all image files
images, labels = load_data("/Volumes/Seagate/Databases/gtsrb")

# Split data into training and testing sets
labels = tf.keras.utils.to_categorical(labels)
x_train, x_test, y_train, y_test = train_test_split(
    np.array(images), np.array(labels), test_size=TEST_SIZE
)

model = keras.models.load_model('modell1')

probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])

predictions = probability_model.predict(x_test)

for i in range(4):
    print(f"Prediction i =",i, "guess =", np.argmax(predictions[i]),"probabality = ", max(predictions[i]))
    print("Label i =", i,"actual_category =", np.argmax(labels[i]))
    cv2.imshow("Image", images[i])
    k = cv2.waitKey(10)
    if k == ord("s"):
        cv2.imwrite("starry_night.png", images[i])
