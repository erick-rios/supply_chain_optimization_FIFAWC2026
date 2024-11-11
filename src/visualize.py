import json
import folium

class MapVisualizer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.places = []
        self.connections = set()  # Para rastrear las conexiones ya trazadas

    def load_data(self):
        """Carga los datos del archivo JSON y los guarda en la lista de lugares."""
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        for place_data in data:
            name = place_data['Name']
            latitude = place_data['Latitude']
            longitude = place_data['Longitude']
            
            # Procesar vecinos y costos
            neighbors = place_data['Neighbors']  # Ya es una lista
            costs = place_data['Cost']  # Ya es una lista
            
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

    def create_map(self):
        """Crea y retorna un objeto de mapa `folium` con los lugares y sus conexiones."""
        if not self.places:
            raise ValueError("No hay datos cargados. Ejecute load_data() primero.")

        # Centrar el mapa en la primera ubicación
        m = folium.Map(location=[self.places[0]["latitude"], self.places[0]["longitude"]], zoom_start=6)

        # Añadir marcadores para cada lugar
        for place in self.places:
            folium.Marker(
                [place["latitude"], place["longitude"]],
                popup=place["name"],
                tooltip=place["name"],
                icon=folium.Icon(color="blue")
            ).add_to(m)

        # Añadir líneas y etiquetas para cada conexión
        for place in self.places:
            for neighbor, cost in place["connections"]:
                # Verificar si el vecino existe en la lista
                neighbor_place = next((p for p in self.places if p["name"] == neighbor), None)
                if neighbor_place:
                    # Evitar duplicar conexiones en ambas direcciones
                    if (place["name"], neighbor) not in self.connections and (neighbor, place["name"]) not in self.connections:
                        # Coordenadas para la línea entre el nodo y su vecino
                        start = [place["latitude"], place["longitude"]]
                        end = [neighbor_place["latitude"], neighbor_place["longitude"]]

                        # Dibujar línea con flecha
                        folium.PolyLine(
                            [start, end],
                            color="red",
                            weight=2,
                            opacity=0.7
                        ).add_to(m)

                        # Añadir el costo de la conexión
                        mid_point = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2]
                        folium.Marker(
                            mid_point,
                            icon=folium.DivIcon(html=f'<div style="font-size: 10pt; color: black;">{cost}</div>')
                        ).add_to(m)

                        # Marcar esta conexión como procesada en ambas direcciones
                        self.connections.add((place["name"], neighbor))
                        self.connections.add((neighbor, place["name"]))
                else:
                    print(f"Advertencia: Vecino '{neighbor}' de '{place['name']}' no encontrado en datos.")

        return m

    def save_map(self, file_name="../images/network_map.html"):
        """Guarda el mapa en un archivo HTML."""
        network_map = self.create_map()
        network_map.save(file_name)
        print(f"Mapa guardado como {file_name}")

# Ejemplo de uso
if __name__ == "__main__":
    visualizer = MapVisualizer("archivo.json")  # Reemplaza con la ruta a tu archivo JSON
    visualizer.load_data()
    visualizer.save_map("network_map.html")
