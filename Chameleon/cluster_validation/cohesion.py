import networkx as nx
import sys
import os
from pathlib import Path
import pandas as pd
sys.path.append('../')


# Defaut edge weight = 1

def get_cohesion(G:nx.Graph()):
    cohesion = 0
    for e in G.edges:
        cohesion = cohesion + 1
    return cohesion