import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from os import path
import sys
sys.path.append('../../')
from Evaluation.silhouette_coefficient import silhoutte_result
def read_snnArray(file_path=None):
    df = pd.read_csv(file_path,index_col=False,header=None,sep=' ')
    snn_nparray = np.array(df)
    return snn_nparray

# Create A dataset contain #number_of_nodes, only 1 column    
def read_dataset(number_of_nodes):
    data = [int(i) for i in range(0,number_of_nodes)]
    dataset = pd.DataFrame(data).to_numpy()
    return dataset
    # print(self.dataset)

def metric(x,y,snn_nparray):
    a = int(x[0])
    b = int(y[0])
    # print(a)
    # print(b)
    if (snn_nparray[a][b]!=0):
        print(a)
        print(b)
        print(snn_nparray[a][b])
    return snn_nparray[a][b]



def dbscan(MinPts,Eps,snn_nparray):
    # a = DBSCAN(eps=Eps,min_samples=MinPts,metric=metric,metric_params={'snn_nparray':snn_nparray}).fit(dataset)
    a = DBSCAN(eps=Eps,min_samples=MinPts,metric='precomputed').fit(snn_nparray)
    return a


if __name__=='__main__':
    # A = SNN_Density()
    # A = read_dataset(9498)
    snn_nparray = read_snnArray('/Users/vankhaido/HUST/GR2/Code/SNN-density/snn_computation/snn_distance_metric.csv')
    data_labeled = dbscan(MinPts=7,Eps=0.75,snn_nparray=snn_nparray)
    labels = data_labeled.labels_
    print(labels)
    # print("\nLABEL")
    for i in labels:
        if (i!=-1):
            print(i)
    silhoute = silhoutte_result(snn_nparray,labels)
    print("Silhoute Score: ",silhoute)
