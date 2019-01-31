import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_nodes_from([3, 4, 5, 6])
G.add_cycle([1, 2, 3, 4])
G.add_edge(1, 3)
G.add_edges_from([(3, 5), (3, 6), (6, 7)])
nx.draw(G, pos=nx.spring_layout(G))
plt.show()

