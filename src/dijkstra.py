# dijkstra.py
from src.heapq import MinHeap

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start, end):
        # Inicialización
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        previous_nodes = {node: None for node in self.graph}
        
        # Inicializamos la cola de prioridad con el nodo de inicio
        min_heap = MinHeap()
        min_heap.push((0, start))

        while not min_heap.is_empty():
            current_distance, current_node = min_heap.pop()

            # Si encontramos el nodo destino, podemos detenernos
            if current_node == end:
                break

            # Si encontramos una distancia más larga, la ignoramos
            if current_distance > distances[current_node]:
                continue

            # Explorar los vecinos
            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                # Si encontramos un camino más corto, actualizamos la distancia
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    min_heap.push((distance, neighbor))

        # Reconstruir el camino
        path = self._reconstruct_path(previous_nodes, start, end)
        return path, distances[end] if distances[end] != float('inf') else (None, float('inf'))

    def _reconstruct_path(self, previous_nodes, start, end):
        """Reconstruye el camino desde el nodo destino hasta el nodo de inicio."""
        path = []
        current_node = end
        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        
        path = path[::-1]  # Invertimos el camino para el orden correcto
        if path[0] == start:  # Verificamos si hay un camino válido
            return path
        return None

# Ejemplo de uso
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    dijkstra = Dijkstra(graph)
    start_node = 'A'
    end_node = 'D'

    path, cost = dijkstra.shortest_path(start_node, end_node)
    print("Camino más corto:", path)
    print("Costo del camino:", cost)
