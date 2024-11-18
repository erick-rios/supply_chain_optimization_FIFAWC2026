from typing import Dict, Tuple, List, Optional
from src.heapq import MinHeap

class Dijkstra:
    """
    Implements Dijkstra's algorithm to find the shortest path in a weighted graph.

    Attributes:
        graph (Dict[str, Dict[str, float]]): A dictionary representing the graph,
        where keys are node names, and values are dictionaries of neighbors with edge weights.
    """

    def __init__(self, graph: Dict[str, Dict[str, float]]) -> None:
        """
        Initializes the Dijkstra class with a graph.

        Args:
            graph (Dict[str, Dict[str, float]]): The input graph represented as an adjacency list.
        """
        self.graph = graph

    def shortest_path(self, start: str, end: str) -> Tuple[Optional[List[str]], float]:
        """
        Finds the shortest path and its cost between two nodes.

        Args:
            start (str): The starting node.
            end (str): The target node.

        Returns:
            Tuple[Optional[List[str]], float]: A tuple containing the shortest path as a list of nodes 
            and the total cost. Returns (None, float('inf')) if no path is found.
        """
        # Initialization
        distances: Dict[str, float] = {node: float('inf') for node in self.graph}
        distances[start] = 0
        previous_nodes: Dict[str, Optional[str]] = {node: None for node in self.graph}

        # Priority queue initialization
        min_heap = MinHeap()
        min_heap.push((0, start))

        while not min_heap.is_empty():
            current_distance, current_node = min_heap.pop()

            # Stop if the target node is reached
            if current_node == end:
                break

            # Skip if the distance is not optimal
            if current_distance > distances[current_node]:
                continue

            # Explore neighbors
            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                # Update the shortest distance if a better path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    min_heap.push((distance, neighbor))

        # Reconstruct the shortest path
        path = self._reconstruct_path(previous_nodes, start, end)
        return path, distances[end] if distances[end] != float('inf') else (None, float('inf'))

    def _reconstruct_path(self, previous_nodes: Dict[str, Optional[str]], start: str, end: str) -> Optional[List[str]]:
        """
        Reconstructs the shortest path from the target node back to the starting node.

        Args:
            previous_nodes (Dict[str, Optional[str]]): A dictionary mapping each node to its predecessor.
            start (str): The starting node.
            end (str): The target node.

        Returns:
            Optional[List[str]]: A list representing the shortest path. 
            Returns None if no path is found.
        """
        path: List[str] = []
        current_node = end
        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        
        path = path[::-1]  # Reverse the path to get the correct order
        if path[0] == start:  # Ensure the path is valid
            return path
        return None

# Example of usage
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
    print("Shortest path:", path)
    print("Path cost:", cost)

