from __future__ import division, print_function, absolute_import
import tflearn
import speech_data
import tensorflow as tf
import os #something I +Amine+ added this line , not my idea though

tf.logging.set_verbosity(tf.logging.ERROR)  #I + Amine + added this
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # and this one too

learning_rate = 0.0001
training_iters = 300000  # steps
batch_size = 64

width = 20  # mfcc features
height = 80  # (max) length of utterance
classes = 10  # digits

batch = word_batch = speech_data.mfcc_batch_generator(batch_size)
X, Y = next(batch)
trainX, trainY = X, Y
testX, testY = X, Y #overfit for now

# Network building
net = tflearn.input_data([None, width, height])
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, classes, activation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=learning_rate, loss='categorical_crossentropy')
# Training

### add this "fix" for tensorflow version errors
#col = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)     #I +Amine+ removed this line by comment to avoid 'two variables have the same name' error
#for x in col:                   # I +Amine+ removed this too
 #   tf.add_to_collection(tf.GraphKeys.VARIABLES, x ) # And this one to m + Amine my doing


model = tflearn.DNN(net, tensorboard_verbose=0)
while 1: #training_iters
  model.fit(trainX, trainY, n_epoch=10, validation_set=(testX, testY), show_metric=True,
          batch_size=batch_size)
  _y=model.predict(X)
model.save("tflearn.lstm.model")
print (_y)
print (y)
