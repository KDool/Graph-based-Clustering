import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.metrics import silhouette_score

# To calculate Silhouette Score of a Clustering Algorithm 
# Input should be:
#          1. Distance Metrix precomputed
#          2. Label list


def silhoutte_result(distance_metrix, labels_list):
    score = 0
    score = silhouette_score(distance_metrix,metric='precomputed',labels=labels_list)
    return score 


