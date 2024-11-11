import tkinter as tk
from tkinter import messagebox
from src.dijkstra import dijkstra
from src.visualize import dibujar_mapa_con_ruta
from src.cargar_datos import cargar_datos_json

# Cargar la red desde el archivo JSON
red = cargar_datos_json('data/network_info.json')

# Crear la ventana principal de la aplicación
window = tk.Tk()
window.title("Aplicación de Rutas Óptimas")
window.geometry("800x600")

# Función para seleccionar nodo inicial
def seleccionar_nodo_inicial():
    nodo = nodo_inicial_entry.get()
    print(f"Nodo inicial seleccionado: {nodo}")

# Función para seleccionar nodo final
def seleccionar_nodo_final():
    nodo = nodo_final_entry.get()
    print(f"Nodo final seleccionado: {nodo}")

# Función para calcular la ruta más corta
def calcular_ruta():
    nodo_inicial = nodo_inicial_entry.get()
    nodo_final = nodo_final_entry.get()
    
    try:
        nodo_inicial = str(nodo_inicial)
        nodo_final = str(nodo_final)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese nodos válidos.")
        return
    
    # Usar Dijkstra para obtener la ruta más corta
    ruta = dijkstra(red, nodo_inicial, nodo_final)
    print(f"La ruta más corta es: {ruta}")
    
    # Dibujar la ruta sobre el grafo
    dibujar_mapa_con_ruta(ruta)

# Crear los widgets de la interfaz gráfica
nodo_inicial_label = tk.Label(window, text="Nodo Inicial:")
nodo_inicial_label.pack()

nodo_inicial_entry = tk.Entry(window)
nodo_inicial_entry.pack()

nodo_final_label = tk.Label(window, text="Nodo Final:")
nodo_final_label.pack()

nodo_final_entry = tk.Entry(window)
nodo_final_entry.pack()

# Botón para seleccionar nodo inicial
boton_inicial = tk.Button(window, text="Seleccionar Nodo Inicial", command=seleccionar_nodo_inicial)
boton_inicial.pack()

# Botón para seleccionar nodo final
boton_final = tk.Button(window, text="Seleccionar Nodo Final", command=seleccionar_nodo_final)
boton_final.pack()

# Botón para calcular la ruta
boton_calcular = tk.Button(window, text="Calcular Ruta", command=calcular_ruta)
boton_calcular.pack()

# Ejecutar la ventana
window.mainloop()
