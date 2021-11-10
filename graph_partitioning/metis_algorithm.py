from networkx.algorithms import tree
import networkx as nx
import numpy as np
import pymetis
import metis

from graph_partitioning.create_subgraph import removeEdges

# class MetisPartition:

#     def __init__(self,path_knnMetric=None,membership=None,np_array=None, G=None):
#         self.path_knnMetric = path_knnMetric
#         self.membership = membership
#         self.np_array = np_array
#         self.G = G
#         pass
#     def getAdjacenciesList(self):
#         metis_array = np.genfromtxt(self.path_knnMetric).astype(int)
#         self.np_array = metis_array.tolist()
#         for element in self.np_array:
#             element = np.array(element)

def partitionGraph(G:nx.Graph,nparts=None,recursive=None):
        # if self.path_knnMetric != None:
        #     self.getAdjacenciesList()
        # n_cuts,self.membership = pymetis.part_graph(nparts,adjacency=self.np_array,recursive=recursive)
    n_cuts,membership = metis.part_graph(G,nparts=nparts,recursive=recursive)
    membership = membership
    return n_cuts,membership


# if __name__ == '__main__':
    # P = MetisPartition(path_knnMetric='/Users/vankhaido/HUST/GR2/Code/create_metrics/knn_metric.csv')
    # n_cuts,membership = P.partitionGraph(nparts=2,recursive=True)
    # print(membership)
    # print("Edge cuts: ",n_cuts)
    # print("NP_ARRAY: ",P.np_array)

# adjacency_list = [np.array([4, 2,3, 1]),
#                   np.array([0, 2, 3]),
#                   np.array([4, 3, 1, 0]),
#                   np.array([1, 2, 5, 6]),
#                   np.array([0, 2, 5]),
#                   np.array([1, 4, 5]),
#                   np.array([0, 3, 5]),
#                   np.array([4, 3, 6]),
#                   np.array([5,8,2])]
# metis_array = np.genfromtxt('/Users/vankhaido/HUST/GR2/Code/create_metrics/knn_metric.csv').astype(int)
# list_metis = metis_array.tolist()
# # print(list_metis)
# for element in list_metis:
#     element = np.array(element)
# print(list_metis)

