import plotly.graph_objects as go

import networkx as nx
import visualize_metric
import numpy as np
def drawAGraph(G=None):
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    

if __name__ == '__main__':
    np_array = np.genfromtxt('/Users/vankhaido/HUST/GR2/Code/create_metrics/knn_metric.csv').astype(int)
    # print(np_array)
    G= nx.Graph()
    n = len(np_array)
    visualize_metric.createGraph(np_array,G)
    drawAGraph(G)
    