import sys
from src.dijkstra import Dijkstra
from src.network_model import NetworkModel
from src.visualize import MapVisualizer

def main(json_file: str, start_node: str, end_node: str) -> None:
    """
    Main function to execute the program. It performs the following tasks:
    1. Loads the network data from a JSON file into a graph.
    2. Computes the shortest path between two nodes using Dijkstra's algorithm.
    3. Visualizes the network on a map and saves it as an HTML file.

    Args:
        json_file (str): Path to the JSON file containing the network data.
        start_node (str): The starting node for the shortest path calculation.
        end_node (str): The destination node for the shortest path calculation.
    """
    # Load the graph from the JSON file
    network = NetworkModel()
    network.load_from_json(json_file)

    # Get the graph representation as a dictionary
    graph_dict = network.to_dict()
    #print("Loaded graph representation:", graph_dict)

    # Compute the shortest path between the specified nodes
    dijkstra = Dijkstra(graph_dict)
    path, cost = dijkstra.shortest_path(start_node, end_node)

    # Check if a valid path was found
    if path is not None:
        print(f"Shortest distance between {start_node} and {end_node}: {cost}")
        print("Path:", " -> ".join(path))
    else:
        print(f"No path found between {start_node} and {end_node}.")

    # Create and save the map visualization
    visualizer = MapVisualizer(json_file)
    visualizer.load_data()
    visualizer.save_map("network_map.html")
    print("Map saved as 'network_map.html'.")

if __name__ == "__main__":
    # Read command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python main.py <json_file> <start_node> <end_node>")
        sys.exit(1)

    json_file = sys.argv[1]  # Path to the JSON file
    start_node = sys.argv[2]  # Start node for the path
    end_node = sys.argv[3]  # End node for the path

    # Run the main program
    main(json_file, start_node, end_node)

