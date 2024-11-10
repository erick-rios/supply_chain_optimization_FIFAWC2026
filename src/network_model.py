import json
import networkx as nx

class NetworkModel:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, name, latitude, longitude):
        """Agrega un nodo al grafo con las coordenadas."""
        self.graph.add_node(name, latitude=latitude, longitude=longitude)

    def add_edge(self, from_node, to_node, cost):
        """Agrega una arista con peso entre dos nodos."""
        self.graph.add_edge(from_node, to_node, weight=cost)

    def load_from_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        for node_data in data:
            name = node_data['Name']
            latitude = node_data['Latitude']
            longitude = node_data['Longitude']
            
            # 'Neighbors' y 'Cost' ya son listas, así que las usamos directamente
            neighbors = node_data['Neighbors']
            costs = node_data['Cost']

            # Agregar nodo al grafo si no existe
            if name not in self.graph:
                self.add_node(name, latitude, longitude)

            # Agregar conexiones entre nodos
            for neighbor, cost in zip(neighbors, costs):
                self.add_edge(name, neighbor, cost)

    def to_dict(self):
        """Convierte el grafo en un diccionario de adyacencia compatible con Dijkstra."""
        graph_dict = {}
        for node in self.graph.nodes:
            neighbors = {neighbor: self.graph[node][neighbor]['weight'] for neighbor in self.graph.neighbors(node)}
            graph_dict[node] = neighbors
        return graph_dict

