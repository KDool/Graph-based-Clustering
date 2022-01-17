# Main.py : - Read data from file by read_data.py ---> return an datafrae
#           - Make similarity metric from data frame by similarity_metric.py , convert to Numpy array --> file .csv
#           - Create knn metric from file csv

import read_data
import similarity_metric
import knn_metric

import pandas as pd
import numpy as np
from os import path


if __name__ == '__main__':
    DE = read_data.ReadData(path='/Users/vankhaido/HUST/GR2/TwitterDataset/DE/DE_')
    nparray_data =  DE.get_df_general()
    # print(nparray_data)
    similarity_result = similarity_metric.Jaccard_similarity_metric(numpy_array=nparray_data)
    # print(similarity_result)
    knn_result = knn_metric.Knn_metric(similarity_result,k=5)
    df_knn = pd.DataFrame(knn_result)
    df_knn.to_csv('./knn_metric.csv',header=False,sep=' ',index=False)