import keras, sklearn
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Conv1D, BatchNormalization, GlobalAveragePooling1D, Permute, Dropout
from tensorflow.keras.layers import Input, Dense, LSTM, concatenate, Activation
from tensorflow.keras.models import Model


def lstmfcn(window: int = 256, vars: int = 4, num_cells: int = 100):
    ip = Input(shape=(window, vars))
    x = LSTM(num_cells)(ip)
    x = Dropout(0.8)(x)

    y = Permute((2, 1))(ip)
    for i, j in ((128, 8),(256, 5), (128, 3)):
        y = Conv1D(i, j, padding='same', kernel_initializer='he_uniform')(y)
        y = BatchNormalization()(y)
        y = Activation('relu')(y)
    y = GlobalAveragePooling1D()(y)

    z = concatenate([x, y])
    out = Dense(1, activation='sigmoid')(z)
    model = Model(ip, out)
    model.summary()
    return model

def train(X_train, y_train, X_val, y_val, epochs = 10):
    model = lstmfcn(X_train.shape[1], X_train.shape[2])
    model.compile(loss="binary_crossentropy", metrics=[
                    keras.metrics.binary_accuracy], optimizer="adam")
        
    log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
    
    model.fit(X_train, y_train, steps_per_epoch=443, epochs=epochs,
          validation_data=(X_val, y_val), 
          callbacks=[tensorboard_callback, CustomSaver()])
    return model

def evaluate(model, X, y):
    h = np.where(model.predict(X) > 0.5, 1, 0)
    print(sklearn.metrics.classification_report(y, h))
    return sklearn.metrics.confusion_matrix(y, h)

class CustomSaver(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        self.model.save("models/model_{}.hd5".format(epoch))