import sys
from src.dijkstra import Dijkstra
from src.network_model import NetworkModel
from src.visualize import MapVisualizer

def main(json_file, start_node, end_node):
    # Cargar el grafo desde el archivo JSON
    network = NetworkModel()
    network.load_from_json(json_file)

    # Obtener la representación en formato de diccionario
    graph_dict = network.to_dict()
    print("Representación del grafo cargado:", graph_dict)

    # Calcular la ruta mínima entre los nodos
    dijkstra = Dijkstra(graph_dict)
    # Calcular la ruta más corta
    path, cost = dijkstra.shortest_path(start_node, end_node)

    # Verificar si se encontró una ruta válida
    if path is not None:
        print(f"Distancia mínima entre {start_node} y {end_node}: {cost}")
        print("Ruta:", " -> ".join(path))
    else:
        print(f"No se encontró una ruta entre {start_node} y {end_node}.")


    # Crear y guardar el mapa visual
    visualizer = MapVisualizer(json_file)
    visualizer.load_data()
    visualizer.save_map("network_map.html")
    print("Mapa guardado como 'network_map.html'.")


if __name__ == "__main__":
    # Leer argumentos de la consola
    if len(sys.argv) != 4:
        print("Uso: python main.py <archivo_json> <nodo_inicio> <nodo_destino>")
        sys.exit(1)

    json_file = sys.argv[1]  # Ahora tomamos un archivo JSON
    start_node = sys.argv[2]
    end_node = sys.argv[3]

    # Ejecutar el programa principal
    main(json_file, start_node, end_node)

