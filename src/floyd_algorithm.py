#  floyd_algorithm.py
class ShortestPath:
    def __init__(self, supply_network):
        self.network = supply_network
        self.distances = {}
        self.initialize_distances()

    def initialize_distances(self):
        nodes = list(self.network.graph.nodes())
        self.distances = {i: {j: float('inf') for j in nodes} for i in nodes}

        # Distancia de un nodo a sí mismo es 0
        for node in nodes:
            self.distances[node][node] = 0

        # Configura las distancias basadas en las aristas existentes
        for u, v, data in self.network.graph.edges(data=True):
            self.distances[u][v] = data['cost']

    def floyd_warshall(self):
        nodes = list(self.network.graph.nodes())

        for k in nodes:
            for i in nodes:
                for j in nodes:
                    if self.distances[i][j] > self.distances[i][k] + self.distances[k][j]:
                        self.distances[i][j] = self.distances[i][k] + self.distances[k][j]

        return self.distances

    def print_shortest_paths(self):
        print("All pairs shortest paths:")
        for i in self.distances:
            for j in self.distances[i]:
                if self.distances[i][j] == float('inf'):
                    print(f"Path from {i} to {j}: No path")
                else:
                    print(f"Path from {i} to {j}: Cost {self.distances[i][j]}")
