# Download the data. The data is already divided into train and test.
# # The labels are integers representing classes.
# fashion_mnist = keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) = \
#     fashion_mnist.load_data()

# # # Names of the integer classes, i.e., 0 -> T-short/top, 1 -> Trouser, etc.
# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
#     'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# print("Shape: ", train_images[0].shape)
# print("Label: ", train_labels[0], "->", class_names[train_labels[0]])

# img = np.reshape(train_images[0], (-1, 28, 28, 1))