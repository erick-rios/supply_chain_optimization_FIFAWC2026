import json
import folium
from typing import List, Dict, Tuple, Any, Set

class MapVisualizer:
    def __init__(self, file_path: str) -> None:
        """
        Initialize the MapVisualizer with the JSON file path.

        Args:
            file_path (str): Path to the JSON file containing network data.
        """
        self.file_path: str = file_path
        self.places: List[Dict[str, Any]] = []
        self.connections: Set[Tuple[str, str]] = set()  # Tracks already drawn connections

    def load_data(self) -> None:
        """
        Loads data from the JSON file and processes it into a list of places.
        
        Each place includes:
        - Name
        - Latitude and Longitude
        - Connections with neighbors and associated costs
        """
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        for place_data in data:
            name = place_data['Name']
            latitude = place_data['Latitude']
            longitude = place_data['Longitude']
            
            neighbors = place_data['Neighbors']  # List of neighbor names
            costs = place_data['Cost']  # List of costs to neighbors
            
            connections = [
                (neighbor, cost) 
                for neighbor, cost in zip(neighbors, costs)
            ]
            
            self.places.append({
                "name": name,
                "latitude": latitude,
                "longitude": longitude,
                "connections": connections
            })

    def get_marker_color(self, name: str) -> str:
        """
        Determines the marker color based on the name of the place.

        Args:
            name (str): Name of the place.

        Returns:
            str: Color for the marker.
        """
        if name in ["BBVA", "Azteca", "Akron"]:
            return "orange"
        elif name.startswith("Planta"):
            return "green"
        elif name.startswith("Distribuidora"):
            return "blue"
        else:
            return "gray"  # Default color for unknown places

    def create_map(self) -> folium.Map:
        """
        Creates and returns a folium map object with the loaded places and their connections.

        Raises:
            ValueError: If no data is loaded.

        Returns:
            folium.Map: A folium map object with markers and connections.
        """
        if not self.places:
            raise ValueError("No data loaded. Please run load_data() first.")

        # Center the map on the first location
        m = folium.Map(location=[self.places[0]["latitude"], self.places[0]["longitude"]], zoom_start=6)

        # Add markers for each place
        for place in self.places:
            color = self.get_marker_color(place["name"])
            folium.Marker(
                [place["latitude"], place["longitude"]],
                popup=place["name"],
                tooltip=place["name"],
                icon=folium.Icon(color=color)
            ).add_to(m)

        # Add lines and labels for each connection
        for place in self.places:
            for neighbor, cost in place["connections"]:
                neighbor_place = next((p for p in self.places if p["name"] == neighbor), None)
                if neighbor_place:
                    if (place["name"], neighbor) not in self.connections and (neighbor, place["name"]) not in self.connections:
                        start = [place["latitude"], place["longitude"]]
                        end = [neighbor_place["latitude"], neighbor_place["longitude"]]

                        folium.PolyLine(
                            [start, end],
                            color="red",
                            weight=2,
                            opacity=0.7
                        ).add_to(m)

                        mid_point = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2]
                        folium.Marker(
                            mid_point,
                            icon=folium.DivIcon(html=f'<div style="font-size: 10pt; color: black;">{cost}</div>')
                        ).add_to(m)

                        self.connections.add((place["name"], neighbor))
                        self.connections.add((neighbor, place["name"]))
                else:
                    print(f"Warning: Neighbor '{neighbor}' of '{place['name']}' not found in data.")

        return m

    def save_map(self, file_name: str = "../images/network_map.html") -> None:
        """
        Saves the map to an HTML file.

        Args:
            file_name (str): The path and name of the output HTML file.
        """
        network_map = self.create_map()
        network_map.save(file_name)
        print(f"Map saved as {file_name}")

# Example usage
if __name__ == "__main__":
    visualizer = MapVisualizer("archivo.json")
    visualizer.load_data()
    visualizer.save_map("network_map.html")

