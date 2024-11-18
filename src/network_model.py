import json
import networkx as nx
from typing import Dict, List, Union

class NetworkModel:
    def __init__(self) -> None:
        """
        Initializes a NetworkModel with an empty graph using NetworkX.
        """
        self.graph: nx.Graph = nx.Graph()

    def add_node(self, name: str, latitude: float, longitude: float) -> None:
        """
        Adds a node to the graph with its geographical coordinates.

        Args:
            name (str): The name of the node.
            latitude (float): Latitude of the node.
            longitude (float): Longitude of the node.
        """
        self.graph.add_node(name, latitude=latitude, longitude=longitude)

    def add_edge(self, from_node: str, to_node: str, cost: Union[int, float]) -> None:
        """
        Adds a weighted edge between two nodes.

        Args:
            from_node (str): The starting node of the edge.
            to_node (str): The ending node of the edge.
            cost (Union[int, float]): The weight or cost associated with the edge.
        """
        self.graph.add_edge(from_node, to_node, weight=cost)

    def load_from_json(self, file_path: str) -> None:
        """
        Loads nodes and edges from a JSON file and populates the graph.

        The JSON file should contain a list of nodes, each with:
        - 'Name' (str): The name of the node.
        - 'Latitude' (float): The latitude of the node.
        - 'Longitude' (float): The longitude of the node.
        - 'Neighbors' (List[str]): A list of neighboring node names.
        - 'Cost' (List[Union[int, float]]): A list of costs associated with each neighbor.

        Args:
            file_path (str): Path to the JSON file containing the graph data.

        Raises:
            FileNotFoundError: If the file at `file_path` does not exist.
            KeyError: If required keys are missing from the JSON data.
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        for node_data in data:
            name: str = node_data['Name']
            latitude: float = node_data['Latitude']
            longitude: float = node_data['Longitude']
            neighbors: List[str] = node_data['Neighbors']
            costs: List[Union[int, float]] = node_data['Cost']

            # Add the node if it doesn't already exist in the graph
            if name not in self.graph:
                self.add_node(name, latitude, longitude)

            # Add edges between the node and its neighbors
            for neighbor, cost in zip(neighbors, costs):
                self.add_edge(name, neighbor, cost)

    def to_dict(self) -> Dict[str, Dict[str, Union[int, float]]]:
        """
        Converts the graph into an adjacency dictionary format.

        This dictionary format is suitable for algorithms like Dijkstra's:
        {
            'NodeA': {'Neighbor1': weight1, 'Neighbor2': weight2, ...},
            'NodeB': {'Neighbor3': weight3, ...},
            ...
        }

        Returns:
            Dict[str, Dict[str, Union[int, float]]]: Adjacency dictionary representation of the graph.
        """
        graph_dict: Dict[str, Dict[str, Union[int, float]]] = {}
        for node in self.graph.nodes:
            neighbors: Dict[str, Union[int, float]] = {
                neighbor: self.graph[node][neighbor]['weight'] for neighbor in self.graph.neighbors(node)
            }
            graph_dict[node] = neighbors
        return graph_dict
