import networkx as nx
import matplotlib.pyplot as plt 

def plot(G:nx.Graph):
    # pos=nx.spring_layout(G)
    pos=nx.spring_layout(G)
    nx.draw(G,pos,with_labels=True,node_size=10)
    # nx.draw(G, pos, node_size=300, with_labels=True)
    plt.show()