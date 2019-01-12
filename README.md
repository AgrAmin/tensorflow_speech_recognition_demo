# tensorflow_speech_recognition_demo
This is the code for 'How to Make a Simple Tensorflow Speech Recognizer' by @Sirajology on Youtube
#----------------------------------------------------------------------------------------------------------------------------

#### * I modified slightly the code in both files but the program didn't work properly in the end:
          -speech_data.py : I changed line to put an updated link for the data since the privious link is expired
          -demo.py : various error happened :
              -> errors about "urlib" and "keep_dims" related to a problem of compatibility of the Tensorflow version 
                  ->"urllib.request fails"
                  ->"urllib.error.URLError: <urlopen error [WinError 10060]" Data download link is not working -fixed
              -> in general use python 3.6 works fine with Tensorflow (3.7 didn't allow to install tensorflow correctly)
              -> error :"Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2" fixed following the recommended solution here "https://stackoverflow.com/questions/47068709/your-cpu-supports-instructions-that-this-tensorflow-binary-was-not-compiled-to-u"
              -> "ValueError: At least two variables have the same name: FullyConnected/W" fixed using this link "https://github.com/llSourcell/tensorflow_speech_recognition_demo/issues/30"
              -> and finally : "RuntimeError: can't start new thread" no fix for that yet. I know what it means, I don't know how to fix it yet. The program runs the training algorithm non stop until it reach that error after several hours (12 hours or so)
#---------------------------------------------------------------------------------------------------------------------------
Overview
============
This is the full code for 'How to Make a Simple Tensorflow Speech Recognizer' by @Sirajology on [Youtube](https://youtu.be/u9FPqkuoEJ8).
In this demo code we build an LSTM recurrent neural network using the TFLearn high level Tensorflow-based library to train
on a labeled dataset of spoken digits. Then we test it on spoken digits. 

Dependencies
============
* tflearn (http://tflearn.org/)
* tensorflow  (https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html)
* future

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies

Usage
===========

Run the following code in terminal. This will take a couple hours to train fully.

`python demo.py`


Challenge
===========

The weekly challenge is from the last video, it's still running! Check it out [here](https://www.youtube.com/watch?v=mGYU5t8MO7s)

Credits
===========
Credit for the vast majority of code here goes to [pannouse](https://github.com/pannous). I've merely created a wrapper to get people started!
