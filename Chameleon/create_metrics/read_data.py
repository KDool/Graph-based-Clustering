from os import path
from numpy.core.numeric import count_nonzero
import pandas as pd
import numpy as np

class ReadData:
    def __init__(self,path,array_general=None, df_original_nodes=None,df_edges=None):
        self.path = path
    
    # read all the nodes in Dataset that have all information
    def read_nodes(self):
        self.df_original_nodes = pd.read_csv(self.path + 'target.csv')
        return self.df_original_nodes
    # read all the edges to other nodes from Dataset
    def read_edges(self):
        self.df_edges = pd.read_csv(self.path + 'edges.csv')
        return self.df_edges
    # Build a general nodes included Original nodes and new related nodes
    def get_df_general(self):
        df_edges = self.read_edges()
        df_nodes = self.read_nodes()
        size_metric = df_nodes['new_id'].max()   # get all nodes related to all the edge
        print("SIZE: ",size_metric)
        array_general= np.zeros((size_metric+1,size_metric+1))
        for index, row in df_edges.iterrows():
            array_general[row['from']][row['to']] = 1
        self.array_general = array_general

        return array_general
if __name__ == '__main__':
    DE = ReadData(path='/Users/vankhaido/HUST/GR2/TwitterDataset/DE/DE_')
    df_nodes = DE.read_nodes()
    df_edges = DE.read_edges()
    # print(df_edges['to'].max())
    df_general = DE.get_df_general()
    print(df_general)
    # row_totals = df_general.sum(axis=1)
# display the array and the sum

    # print("Sum of each row:", row_totals)
