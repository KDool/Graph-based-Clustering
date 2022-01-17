# Tính similairy giữa các data points
# Input: File.csv
# Các modules: Euclidean Distance(dis-similarity), Jaccard Similarity,
# 
import pandas as pd
import numpy as np
from threading import Thread
from sklearn.metrics import jaccard_score
from scipy.spatial.distance import euclidean, pdist, squareform
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


def similarity_func(u, v):
    return 1/(1+euclidean(u,v))

def Euclidean_similarity_metric(numpy_array=None):
    # Calculate all pairwise distances
    euclidean_similarity = pdist(numpy_array,metric='euclidean')
    
    # #Convert the distances to a square matrix
    euclidean_similarity= squareform(euclidean_similarity)
    return euclidean_similarity