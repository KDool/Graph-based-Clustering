from typing import List
import numpy as np
import networkx as nx
import sys
import os
from pathlib import Path
sys.path.append('../')
from graph_partitioning.create_Graphnetworkx import Graph
# from graph_partitioning.metis_algorithm import MetisPartition
from graph_partitioning import metis_algorithm
import matplotlib.pyplot as plt
import random
import pandas as pd

def removeEdges(Graph: nx.Graph, membership=list):
    G = Graph.copy()
    count = 0
    df = pd.DataFrame(G.nodes(data=False)) 
    # list_nodes = df[0].values.tolist()
    for e in G.edges:
        index_u = df.index[df[0]==e[0]][0]
        index_v = df.index[df[0]==e[1]][0]
        if membership[index_u] != membership[index_v]:
            # print(e[0],e[1])
            G.remove_edge(e[0],e[1])
            count +=1
    print("Edges removed: ",count)
    return G

# def get_cmap(n, name='hsv'):
#     '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
#     RGB color; the keyword argument name must be a standard mpl colormap name.'''
#     return plt.cm.get_cmap(name, n)

def get_cmap(membership:list):
    number_of_colors = len(unique(membership))
    
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        for i in range(number_of_colors)]
    return color
def make_colorMap(G: nx.Graph,membership=list):
    # cmap = get_cmap(membership)
    cmap = get_cmap(membership)
    # print(cmap(0))
    df = pd.DataFrame(G.nodes(data=False)) 
    color_map = []
    for node in G.nodes:
        index_node = df.index[df[0]==node][0]
        color_map.append(cmap[membership[index_node]])
        # print(node)
    return color_map

def unique(list1):
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

# Create a list of sub graphs after metis partition 
def make_subgraphs(G:nx.Graph,membership:list):
    graphs_label = unique(membership)   ## get unique list of sub-graphs
    graphs_list = [None]*len(graphs_label)                    # a list of subgraphs

    df = pd.DataFrame(G.nodes(data=False)) 
    # list_nodes = df[0].values.tolist()
    for id in graphs_label:
        temp = nx.Graph()
        for node in G.nodes:
            index_node = df.index[df[0]==node][0]
            if(membership[index_node] == id):
                temp.add_node(node)
        for e in G.edges:
            index_u = df.index[df[0]==e[0]][0]
            index_v = df.index[df[0]==e[1]][0]
            if (membership[index_u] == membership[index_v]) and (membership[index_u] == id):
                temp.add_edge(e[0],e[1])
        graphs_list[id]= temp

    return graphs_list




if __name__ == '__main__':

    graph = Graph(file_path='/Users/vankhaido/HUST/GR2/Code/Chameleon/create_metrics/knn_metric.csv')
    G = graph.createGraphFromFile()
    print(G)
    
    n_cuts,membership = metis_algorithm.partitionGraph(G,nparts=100,recursive=True)
    print(membership)
    print(n_cuts)
    subgraphs = make_subgraphs(G,membership)
    # print(subgraphs)
    for i in range(0,len(subgraphs)):
        print(subgraphs[i])

    # # print(membership)

    # # print("Membership 5754: ",membership[5754])
    # # print("Membership 4946: ",membership[0])

    # G2 = removeEdges(G,membership)
    # print(G2)

    # # print(G2.has_edge(4806,5754))
    # # #Make color map 
    # print((unique(membership)))
    
    # color_map = make_colorMap(G,membership)
    # print(unique(color_map))
    # # print(color_map)
    # nx.draw(G2,with_labels=False,node_color=color_map,node_shape="s",node_size=10)
    # plt.show()