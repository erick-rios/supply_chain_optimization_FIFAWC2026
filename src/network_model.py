# network_model.py
import networkx as nx

class SupplyNetwork:
    def __init__(self):
        self.graph = nx.DiGraph()  # Directed graph for supply chain

    def add_node(self, node_id, node_type):
        self.graph.add_node(node_id, type=node_type)

    def add_edge(self, from_node, to_node, cost, capacity):
        self.graph.add_edge(from_node, to_node, cost=cost, capacity=capacity)

    def display_network(self):
        print("Nodes:", self.graph.nodes(data=True))
        print("Edges:", self.graph.edges(data=True))
