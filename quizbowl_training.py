#imports
import numpy as np
import random
import keras.models
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
import sys

#open text file with poems
text = (open("quizbowl.txt").read()).lower()
text = text.split(' ')
#sort list of unique characters in text
chars = sorted(list(set(text)))
print(chars)
#dictionary mapping chars to ints
char_to_int = {char:n for n,char in enumerate(chars)}
#dictionary mapping ints to chars
int_to_char = {n:char for n,char in enumerate(chars)}

#training and target lists
X,y = [],[]
text_length = len(text)
#length of string given to NN to make prediction
str_length = 25
print("Unique chars:", len(chars))
print("Text length:", text_length)

#loop through text
for i in range(0, text_length - str_length, 1):
    #add a list of length str_length to training data
    X.append([char_to_int[c] for c in text[i : i + str_length]])
    #add the next character in the sequence to target list
    #y[n] will have the character that comes after x[n][str_length-1]
    #we want the NN to predict the next letter based on previous letters
    y.append(char_to_int[text[i + str_length]])

#reshape training data for the NN
X_2 = np.reshape(X, (len(X), str_length, 1))
#normalize the training data so that all values are between 0 and 1
X_2 = X_2 / float(len(chars))
#convert Y to a one-hot array··
y_2 = np_utils.to_categorical(y)
print('Data loaded')


#Keras NN
model = Sequential()
#add long short term memory cell
#output_shape is (_, 700), input_shape is (number_of_inputs, input_length), return full sequence
model.add(LSTM(50, input_shape=(X_2.shape[1], X_2.shape[2]), return_sequences=True)) #layer 1
#account for overfitting
model.add(Dropout(0.2))

#add another LSTM layer
model.add(LSTM(50, return_sequences=True)) #layer 2
#account for overfitting
model.add(Dropout(0.2))

#add another LSTM layer
model.add(LSTM(50)) #layer 3
#account for overfitting
model.add(Dropout(0.2))

#Fully connected (dense) output layer
model.add(Dense(y_2.shape[1], activation='softmax')) #layer 4
#minimize loss
model.compile(loss='categorical_crossentropy', optimizer='adam')
print("Model compiled")

filepath = "current_word_50_50_50.h5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

#train the model
model.fit(X_2, y_2, epochs=1000, batch_size=128, callbacks=callbacks_list)
#save the model
model.save("final_word_50_50_50.h5")
print("Training Completed!")
