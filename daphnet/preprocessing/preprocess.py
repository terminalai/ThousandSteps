import sys
import numpy as np
import pandas as pd
from glob import glob

directory = sys.argv[1] if len(sys.argv) > 1 else "daphnet/"

names = ["time"] + sum([[dirn+"_"+loc for dirn in list("xyz")] for loc in ["ankle", "thigh", "trunk"]], []) + ["label"]

columns = ",".join(["label" if i == 768 else f"input{i}" for i in range(769)])

def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

data = np.empty((0, 256*3+1))

filenames = glob(directory + "/*.txt")

batch_size = len(filenames) // 3

batch1 = filenames[:batch_size]
batch2 = filenames[batch_size:2*batch_size]
batch3 = filenames[2*batch_size:]

for i, batch in enumerate([batch1, batch2, batch3]):
    data = np.empty((0, 256*3+1))
    
    for filename in batch:
        df = pd.read_csv(filename, delimiter=" ", names = names)
        X = np.hstack((rolling_window(df.x_thigh.values,256), rolling_window(df.y_thigh.values,256), rolling_window(df.z_thigh.values,256)))
        Y = df.label[:-255]
        X = X[Y != 0]
        Y = (Y[Y != 0] - 1).values.reshape(-1, 1)
        data_temp = np.hstack((X, Y))
        data = np.vstack((data, data_temp))
    
    np.savetxt(directory+f"/data{i}.csv", data, delimiter=",", header=columns, comments="")
    del data







