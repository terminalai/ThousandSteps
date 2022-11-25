from keras.models import Model
from keras.layers import Input, Dense, LSTM, multiply, concatenate, Activation, Masking, Reshape
from keras.layers import Conv1D, BatchNormalization, GlobalAveragePooling1D, Permute, Dropout


MAX_TIMESTEPS = 256
MAX_NB_VARIABLES = 3
NB_CLASS = 2

