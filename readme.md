# Predicting Traffic Signs

I've started with a CNN lookin like this:
![NN](NN.png)

Total Params = 610,000

It shows good accuracy ~0.946. But i do think that something is wrong.
I build prediction.py that makes predictions on test images and it is completly off.
I got best probabilities around 0.96.

I need to explore and i decided to build a TensorBoard to have some insight.
I've experiencing a lot of trouble with tf.keras.callbacks.LambdaCallback(on_epoch_end=log_confusion_matrix) and eventually gave up on idea with confusion matrix. 

Spend an evening on the module tf.keras.preprocessing.image_dataset_from_directory to eventually find out that it doesn't work with ppm files. Must read docs carefully. Considering contribute a warning message of file formats instead of just "No image Found".

Ok, geeting to understand push/pull requests in git and PEP 8.
Made changes to original code. How to run pylint?
Posted my request.

Few weeks later, i thought about doing more experiments and so using notebooks for that(saves time to load data).

The model was build on top of tf tutorials and advice found by googling for similiar tasks. Also i have a book on AI by Moroney, which was a great help for this project. One of the first chapters is about CNN.

I have quite decent result with layers: 
Conv2D(16,(3)), 
MaxPolling(2), 
Conv2d(64,(3)),
MaxPolling(2), 
FLatten,
Dense(256),
Dropout(0.2)
Output(NUM_CATEGORIES): 
Accuracy is 0.95.
Compilation: "ada,", "categorical_crossentropy", "accuracy". Here i suppose i can only play with optimizer.

Following the rule "Just keep adding layers until the test error does not improve anymore."
I will add more layers: 
Conv2D(16,(3)), 
MaxPolling(2), 
Conv2d(64,(3)),
MaxPolling(2), 
FLatten,
Dense(256), 
Dense(512),
Dropout(0.2)
Output(NUM_CATEGORIES) Accuracy is 0.97.
Total params: 753,451

I will add even more layers:  
Conv2D(16,(3)), 
MaxPolling(2), 
Conv2d(64,(3)),
MaxPolling(2),
Conv2d(128,(3)),
MaxPolling(2),
FLatten,
Dense(256), 
Dense(512),
Dropout(0.2)
Output(NUM_CATEGORIES) Accuracy is 0.95. 
It became worse! Let's change smthing. Also quite a drop in total params to 368,555

I removed last MaxPooling(2):  
Conv2D(16,(3)), 
MaxPolling(2), 
Conv2d(64,(3)),
MaxPolling(2),
Conv2d(128,(3)),
FLatten,
Dense(256), 
Dense(512),
Dropout(0.2)
Output(NUM_CATEGORIES) Accuracy is 0.96. 
It a bit beter! Let's change smthing.

This layer looks like variant 2:
Conv2D(16,(3)), 
MaxPolling(2), 
Conv2d(64,(3)),
MaxPolling(2), 
FLatten,
Dense(256), 
Dense(512),
Dense(256), 
Dropout(0.2)
Output(NUM_CATEGORIES) Accuracy is 0.95.

Changing last dense layer to 1024 neurons:
Conv2D(16,(3)), 
MaxPolling(2), 
Conv2d(64,(3)),
MaxPolling(2), 
FLatten,
Dense(256), 
Dense(512),
Dense(256), 
Dropout(0.2)
Output(NUM_CATEGORIES) Accuracy is 0.94.