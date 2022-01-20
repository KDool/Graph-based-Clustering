from networkx.readwrite.json_graph import adjacency
import numpy as np
import math
import networkx as nx
import sys
import os
from pathlib import Path
import pandas as pd
sys.path.append('../')
import metis

# Calculate SEC(Ci,Cj)
def countEdgesBetweenClusters(G:nx.Graph(),subgraphs:list,sub_g1: nx.Graph(),sub_g2: nx.Graph(),membership:list):
    
    id1 = subgraphs.index(sub_g1)          # get ID of cluster 1
    id2 = subgraphs.index(sub_g2)          # get ID of cluster 2
    count = 0
    df = pd.DataFrame(G.nodes(data=False)) 
    for e in G.edges:
        # index_u = df.index[df[0]==e[0]][0]
        # index_v = df.index[df[0]==e[1]][0]
        index_u = e[0]
        index_v = e[1]
        if (membership[index_u] == id1 and membership[index_v] == id2) or (membership[index_v] == id2 and membership[index_u] == id1):
            count += 1 
            # If an edge of original graph contains 2 vertices belong to sub_g1, sub_g2 --> count+1 
    return count 

# Calculate SEC(Ci)
def countEdgesCutBisector(Ci:nx.Graph):
    n_cuts,membership = metis.part_graph(Ci,nparts=2,recursive=True)
    return n_cuts
    # print(membership)

def RC(G:nx.Graph(),subgraphs:list,sub_g1:nx.Graph(),sub_g2:nx.Graph(),membership:list):
    m1 = sub_g1.number_of_nodes()
    m2 = sub_g2.number_of_nodes()
    sec_12 = countEdgesBetweenClusters(G=G,subgraphs=subgraphs,sub_g1=sub_g1,sub_g2=sub_g2,membership=membership)  
    sec_1 = countEdgesCutBisector(sub_g1)
    sec_2 = countEdgesCutBisector(sub_g2)

    rc = sec_12/((m1/(m1+m2))*sec_1 + (m2/(m1+m2))*sec_2)
    return rc


    # print(countEdgesCutBisector(G))
   
  
    