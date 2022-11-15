import tensorflow as tf
import keras
from tensorflow.keras.layers import Conv1D, BatchNormalization, GlobalAveragePooling1D, Permute, Dropout
from tensorflow.keras.layers import Input, Dense, LSTM, concatenate, Activation, Bidirectional
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