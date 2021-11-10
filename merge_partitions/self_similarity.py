from networkx.readwrite.json_graph import adjacency
import numpy as np
import math
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
from merge_partitions.relative_interconnectivity import RI
from merge_partitions.relative_closeness import RC

def get_selfsimilarity(RC,RI,alpha):
    self_similarity = RC * (RI**alpha)
    return self_similarity

if __name__ == '__main__':
    graph = Graph(file_path='/Users/vankhaido/HUST/GR2/Code/create_metrics/knn_metric.csv')
    G = graph.createGraphFromFile()
    print(G)
    n_cuts,membership = metis_algorithm.partitionGraph(G,nparts=4,recursive=False)
    subgraphs = sg.make_subgraphs(G,membership)
    rc = RC(G=G,subgraphs=subgraphs,sub_g1=subgraphs[1],sub_g2=subgraphs[2],membership=membership)
    ri = RI(G=G,subgraphs=subgraphs,sub_g1=subgraphs[1],sub_g2=subgraphs[2],membership=membership)
    ss = get_selfsimilarity(rc,ri,2)
    print(ss)