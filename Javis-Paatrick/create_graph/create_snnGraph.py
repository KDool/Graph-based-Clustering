import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from os import path
import sys
sys.path.append('../')

# def readCSVtoNumpy(file_path=''):
#     np_array = np.genfromtxt(file_path).astype(int)
#     return np_array

def readData(file_path=''):
    df = pd.read_csv(file_path,index_col=False,header=None,sep=' ')
    np_array = np.array(df)
    return np_array

def createGraph(np_array:np.array):
    number_of_nodes = len(np_array)
    G = nx.Graph()
    for e in range(0,number_of_nodes):
        G.add_node(e)
    
    for i in range(0,number_of_nodes):
        for j in range(i+1,number_of_nodes):
            if np_array[i][j]!= 0:
                G.add_edge(i,j,weight=np_array[i][j])
    return G


# def makeGraph()



    