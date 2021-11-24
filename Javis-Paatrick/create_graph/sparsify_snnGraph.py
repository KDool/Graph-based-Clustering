import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from os import path
import sys
sys.path.append('../')


def sparsifyGraph(G:nx.Graph(),threshold:int):
    g = G.copy()
    edges_list = list(g.edges(data=True))
    for e in edges_list:
        if e[-1]['weight'] < threshold:
            g.remove_edge(e[0],e[1])
    return g
