# Tính similairy giữa các data points
# Input: File.csv
# Các modules: Euclidean Distance(dis-similarity), Jaccard Similarity,
# 
import pandas as pd
import numpy as np
import read_data
from threading import Thread
from sklearn.metrics import jaccard_score
from scipy.spatial.distance import pdist, squareform
def Jaccard_similarity(lista=None,listb=None):
    intersection = np.logical_and(lista, listb)
    union = np.logical_or(lista, listb)
    similarity = intersection.sum() / float(union.sum())
    return similarity 

def SMC_similarity(lista=None,listb=None):
    axorb = np.logical_xor(lista,listb)  # 01,10
    total_bits = len(lista)
    similarity = (total_bits - axorb.sum())/total_bits   
    return similarity



def Jaccard_similarity_metric(numpy_array=None):
    # Calculate all pairwise distances
    jaccard_distances = pdist(numpy_array, metric='jaccard')
 
    # Convert the distances to a square matrix
    jaccard_distances = squareform(jaccard_distances)
    jaccard_similarity = 1-jaccard_distances
    return jaccard_similarity

def SMC_similarity_metric(numpy_array=None):
    SMC_similarity = pdist(numpy_array,metric='')
    return 0




# Define some binary vectors
x = [0,1,0,1,0,1,0,0,1]
y = [0,0,1,1,0,0,0,0,1]
z = [1,1,0,0,0,1,0,0,0]

if __name__=='__main__':
    # simxy = Jaccard_similarity(x,y)
    # smcxy = SMC_similarity(x,y)
    # print('Jaccard Similarity of x and y: ',simxy)
    # print('SMC Similarity of x and y: ',smcxy)
    DE = read_data.ReadData(path='/Users/vankhaido/HUST/GR2/TwitterDataset/DE/DE_')
    nparray_data =  DE.get_df_general()


    array = np.array([[1,1,1,0,1,0,0,1],
         [1,1,0,0,1,1,1,0],
         [0,0,1,1,1,0,1,1],
         [1,0,1,1,0,0,0,1],
         [1,0,1,0,1,1,0,1],
         [1,0,1,0,1,1,0,1],
         [0,1,1,0,1,0,1,0],
         [1,0,1,1,0,0,1,1]])

    similarity_result = Jaccard_similarity_metric(nparray_data)
    similarity_result = Jaccard_similarity_metric(array)
    print(similarity_result)
