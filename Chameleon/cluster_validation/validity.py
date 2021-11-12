# Get the overall validity of clusters
from operator import sub
import sys
import os
from pathlib import Path
sys.path.append('../')
from cluster_validation import cohesion
from cluster_validation import separation
from graph_partitioning import metis_algorithm
import graph_partitioning.create_subgraph as sg
from graph_partitioning.create_Graphnetworkx import Graph

import networkx as nx
import itertools

def get_validityOfCohesion(G:nx.Graph(),subgraphs:list):
    total_validity = 0

    for g in subgraphs:
        if g!= None:
            total_validity = total_validity + cohesion.get_cohesion(g)/g.number_of_nodes()
    return total_validity

def get_validityOfSeparation(G:nx.Graph(),subgraphs:list,membership:list):
    total_validity = 0
    for sub_g in subgraphs:
        total_validity = total_validity + separation.get_separation(G=G,subgraphs=subgraphs,sub_g1=sub_g,membership=membership)/cohesion.get_cohesion(sub_g)
    return total_validity

def sumab(a,b):
    return a+b

if __name__ == '__main__':

    graph = Graph(file_path='/Users/vankhaido/HUST/GR2/Code/create_metrics/knn_metric.csv')
    G = graph.createGraphFromFile()
    print(G)
    n_cuts,membership = metis_algorithm.partitionGraph(G,nparts=4,recursive=False)
    subgraphs = sg.make_subgraphs(G,membership)
    # cohesion = cohesion.get_cohesion(G)
    # ri = RI(G=G,subgraphs=subgraphs,sub_g1=subgraphs[1],sub_g2=subgraphs[2],membership=membership)
    # ss = get_selfsimilarity(rc,ri,2)
    valid_cohesion = get_validityOfCohesion(G=G,subgraphs=subgraphs)
    valid_separation = get_validityOfSeparation(G=G,subgraphs=subgraphs,membership=membership)
    print("Valid Cohesion: ",valid_cohesion)
    print("Valid Separation: ",valid_separation)
    