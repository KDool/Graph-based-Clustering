import numpy as np
import pandas as pd
import read_data
import similarity_metric

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


if __name__ == '__main__':
    DE = read_data.ReadData(path='/Users/vankhaido/HUST/GR2/TwitterDataset/DE/DE_')
    nparray_data =  DE.get_df_general()
    similarity_result = similarity_metric.Jaccard_similarity_metric(nparray_data)

    knn_result = Knn_metric(similarity_result,k=3)

    
    # print(similarity_result[0])
    # knn = Knn_vector(similarity_result[0],7)
    # print(knn)
    # B = np.empty((0,3))
    # a = np.array([1,2,3])
    # b = np.array([3,4,5])
    # B = np.vstack((B,a))
    # B = np.vstack((B,b))
    # c = np.concatenate((a,b))
    df_knn = pd.DataFrame(knn_result)
    df_knn.to_csv('./knn_metric.csv',header=False,sep=' ',index=False)
    # print('knn metrics is: \n',knn_result)