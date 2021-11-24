import create_snnGraph as cs
import sparsify_snnGraph as ss
import plot_graph as pg
import networkx as nx




if __name__=='__main__':
    a = cs.readData('../snn_computation/snn_metric.csv')
    print(a)
    G = cs.createGraph(a)
    # for e in G.edges(data=True):
    #     print(e[-1])
    print("G edges: ",G.number_of_edges())
    print("G nodes: ",G.number_of_nodes())


    # print(g.number_of_edges())
    # for e in g.edges(data=True):
    #     print(e[-1])
    # pg.plot(G)
    g = ss.sparsifyGraph(G,threshold=5)
    # e1 = G.get_edge_data(8465,8636)
    # e2 = G.get_edge_data(8465,8836)
    # e3 = G.get_edge_data(8836,8636)
    # 8465, 8636, 8836    
    # print(e1)
    # print(e2)
    # print(e3)
    sub_graphs = nx.connected_components(g)
    for sub in sub_graphs:
        if(len(sub)>2):
            print(sub)
    # print("g edges: ",g.number_of_edges())
    # print("g nodes: ",g.number_of_nodes())
    # pg.plot(g)