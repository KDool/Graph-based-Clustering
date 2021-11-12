import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Graph:
    def __init__(self,nparray_adjacencies=None,file_path=None):
        self.G = nx.Graph()
        self.file_path = file_path
        self.nparray_adjacencies = nparray_adjacencies
        pass

    def addEdge(self,index, single_nparray):
        n = len(single_nparray)
        for i in range(0,n):
            self.G.add_edge(index,single_nparray[i])
    
    # read graph from Graph file
    def readCSVtoNumpy(self):
        np_array = np.genfromtxt(self.file_path).astype(int)
        return np_array
    # Create network graph from Graph file 
    def createGraphFromFile(self):
        np_array = self.readCSVtoNumpy()
        n = len(np_array)
        for i in range(0,n):
            self.addEdge(i,np_array[i])
        return self.G
    # Create network graph from Nummpy Array of Ajacencies
    def createGraphFromAjacentList(self):
        n = len(self.nparray_adjacencies)
        for i in range(0,n):
            self.addEdge(i,self.nparray_adjacencies[i])
        return self.G

if __name__=='__main__':

    graph = Graph(file_path='/Users/vankhaido/HUST/GR2/Code/create_metrics/knn_metric.csv')
    G = graph.createGraphFromFile()
    print(G)
    # G = graph.
    # graph.createGraph(path='/Users/vankhaido/HUST/GR2/Code/create_metrics/knn_metric.csv')
    # np_array = np.genfromtxt('/Users/vankhaido/HUST/GR2/Code/create_metrics/knn_metric.csv').astype(int)
    # print(np_array)
    # G= nx.Graph()
    # n = len(np_array)
    # node_sizes={}
    # for node in G.nodes:
    #     node_sizes = node_sizes.append(1)
    # createGraph(np_array,G)
    # print(G)
    nx.draw(G,with_labels=True,node_shape="s",node_size=10)
    plt.show()