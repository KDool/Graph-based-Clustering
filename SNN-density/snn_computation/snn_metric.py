# Return a snn_metric - Numpy array
# Each element value is a WEIGHT = Number of shared neighbors between 2 nodes

import numpy as np
import pandas as pd
from os import path
import sys
sys.path.append('../')

# read KNN metric from file csv - Return numpy array
def read_knnMetric(file_path=None):
    df = pd.read_csv(file_path,index_col=False,header=None,sep=' ')
    np_array = df.to_numpy(dtype=int)
    # print(np_array)
    return np_array


# Computer SNN: input nodeA,nodeB, KNN metrics - Return count SNN
def compute_sharedNeighbors(nodeA,nodeB,knn_metric:np.array):
    count = 0
    # print(knn_metric)
    np_A = knn_metric[nodeA]
    np_B = knn_metric[nodeB]
    # print(np_B,np_A)
    if (nodeA in np_B) and (nodeB in np_A):
        # print(True)
        count = np.sum(np_A == np_B)
        # print(count)
    else:
        count = 0
    return count

def create_snnMetric(knn_metric:np.array):
    # n = 
    size = len(knn_metric)
    snn_nparray = np.zeros((size,size),dtype=int)
    for i in range(0,size):
        for j in range(i+1,size):
            snn_nparray[i][j] = compute_sharedNeighbors(i,j,knn_metric=knn_metric)
            snn_nparray[j][i] = snn_nparray[i][j]
    return snn_nparray

def get_snn_similarity(nodeA,nodeB,knn_metric:np.array):
    """Calculate the shared-neighbor similarity of two sets of nearest neighbors, normalized by the maximum number of shared neighbors"""
    shared_nodes = compute_sharedNeighbors(nodeA,nodeB,knn_metric=knn_metric)

    return shared_nodes/len(knn_metric[nodeA])


def get_snn_distance(nodeA,nodeB,knn_metric:np.array):
    """Calculate the shared-neighbor distance of two sets of nearest neighbors, normalized by the maximum number of shared neighbors"""

    return 1 - get_snn_similarity(nodeA,nodeB,knn_metric=knn_metric)

def create_snn_distance(knn_metric:np.array):
    # Calculate distance metrix, implied from shared-nearest neighbor metrix
    size = len(knn_metric)
    snn_nparray = np.zeros((size,size),dtype=float)
    for i in range(0,size):
        for j in range(i+1,size):
            snn_nparray[i][j] = get_snn_distance(i,j,knn_metric=knn_metric)
            snn_nparray[j][i] = snn_nparray[i][j]
    return snn_nparray


if __name__=='__main__':
    np_array = read_knnMetric('../knn_metrics/knn_metric.csv')
    # count = compute_sharedNeighbors(0,2432,np_array)
    # snn_result = create_snnMetric(np_array)
    snn_distance_result = create_snn_distance(np_array)
    print(snn_distance_result)
    df_snn = pd.DataFrame(snn_distance_result)
    df_snn.to_csv('./snn_distance_metric.csv',header=False,sep=' ',index=False)