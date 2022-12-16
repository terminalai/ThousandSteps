import sys
import numpy as np
import pandas as pd
from glob import glob

directory = sys.argv[1] if len(sys.argv) > 1 else "daphnet/"

names = ["time"] + sum([[dirn+"_"+loc for dirn in list("xyz")] for loc in ["ankle", "thigh", "trunk"]], []) + ["label"]


def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

data = np.empty((0, 256*3+1))
for filename in glob(directory+"/*.txt"):
    df = pd.read_csv(filename, delimiter=" ", names = names)
    X = np.hstack(
        (rolling_window(df.x_thigh.values,256), rolling_window(df.y_thigh.values,256), rolling_window(df.z_thigh.values,256))
    )
    Y = df.label[:-255]
    X = X[Y != 0]
    Y = (Y[Y != 0] - 1).values.reshape(-1, 1)
    data_temp = np.hstack((X, Y))
    data = np.vstack((data, data_temp))


np.savetxt(directory+"/data.csv", data, delimiter=",")


