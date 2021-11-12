import numpy as np
import networkx as nx
import sys
import os
from pathlib import Path
import pandas as pd
sys.path.append('../')


# in the default, edge weight =  1
def single_separation(G:nx.Graph(),subgraphs:list,sub_g1: nx.Graph(),sub_g2: nx.Graph(),membership:list):
    
    if sub_g1 == None or sub_g2 == None:
        return 0
    if sub_g1 == sub_g2:
        return 0       
    id1 = subgraphs.index(sub_g1)          # get ID of cluster 1
    id2 = subgraphs.index(sub_g2)          # get ID of cluster 2
    count = 0
    df = pd.DataFrame(G.nodes(data=False)) 
    for e in G.edges:
        index_u = df.index[df[0]==e[0]][0]
        index_v = df.index[df[0]==e[1]][0]
        if (membership[index_u] == id1 and membership[index_v] == id2) or (membership[index_v] == id2 and membership[index_u] == id1):
            count += 1 
            # If an edge of original graph contains 2 vertices belong to sub_g1, sub_g2 --> count+1 
    return count 

def get_separation(G:nx.Graph(),subgraphs:list,sub_g1: nx.Graph(),membership:list):

    sep = 0
    for g in subgraphs:
        sep = sep + single_separation(G=G,subgraphs=subgraphs,sub_g1=sub_g1,sub_g2=g,membership=membership)

    return sep