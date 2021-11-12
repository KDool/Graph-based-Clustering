import networkx as nx
import sys
import os
from pathlib import Path

import pandas as pd
sys.path.append('../')
from graph_partitioning.create_Graphnetworkx import Graph
# from graph_partitioning.metis_algorithm import MetisPartition
from graph_partitioning import metis_algorithm
import graph_partitioning.create_subgraph as sg

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

def merge(G:nx.Graph,subgraphs:list,sub_g1:nx.Graph,sub_g2:nx.Graph,membership:list):
    id1 = subgraphs.index(sub_g1)          # get ID of cluster 1
    id2 = subgraphs.index(sub_g2)          # get ID of cluster 2
    id = 0
    new_graph = nx.Graph()
    #choose smaller id as the new id after merge
    if id1<id2:
        id = id1
    else:
        id = id2
    new_graph = nx.compose(sub_g1,sub_g2)
    df = pd.DataFrame(G.nodes(data=False))
    
    # add edges cut before
    for e in G.edges:
        index_u = df.index[df[0]==e[0]][0]
        index_v = df.index[df[0]==e[1]][0]
        if (membership[index_u] == id1 and membership[index_v] == id2) or (membership[index_v] == id2 and membership[index_u] == id1):
            new_graph.add_edge(e[0],e[1])

    # change membership in original graph
    for node in new_graph.nodes:
        index_node = df.index[df[0]==node][0]
        membership[index_node] = id 
    # Update subgraphs list
    subgraphs[id1]= None
    subgraphs[id2]=None
    subgraphs[id]= new_graph

    return new_graph,subgraphs

if __name__ == '__main__':
    graph = Graph(file_path='/Users/vankhaido/HUST/GR2/Code/Chameleon/create_metrics/knn_metric.csv')
    G = graph.createGraphFromFile()
    print(G)
    n_cuts,membership = metis_algorithm.partitionGraph(G,nparts=4,recursive=True)
    subgraphs = sg.make_subgraphs(G,membership)
    for gr in subgraphs:
        print(gr)
    new_gr,subgraphs = merge(G=G,subgraphs=subgraphs,sub_g1=subgraphs[0],sub_g2=subgraphs[1],membership=membership)
    print(new_gr)
    for gr in subgraphs:
        print(gr)