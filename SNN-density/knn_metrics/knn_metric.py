import numpy as np
import pandas as pd
# import read_data
# import similarity_metric

def Knn_vector(nparray=None,k=None):
    # Input: A vector in form of numpy array
    #      : K is number of nearst neighbor
    # Return an array, contain K-nearest neighbors 
    knn_vector = np.argpartition(nparray, -k)[-k:]
    return knn_vector


#make an similarity array in which array[i][i] =0 instead of 1
def cloneArray(nparray=None):
    array_clone = nparray.copy()
    n = len(nparray)
    for i in range (n):
        array_clone[i][i] = 0
    return array_clone

def Knn_metric(nparray=None,k=None):
    # nparray: A Numpy array,
    # K: number of nearest neighbor
    # Return a metric B, contains K-nearest neighbor is 1, none is 0
    nparray_clone = cloneArray(nparray)
    B = np.empty((0,k),int)
    for i in range (0,len(nparray_clone)):
        index = Knn_vector(nparray_clone[i],k)
        B = np.vstack((B,index)) 
    return B
