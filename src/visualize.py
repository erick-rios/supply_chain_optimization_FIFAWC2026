!pip install folium

import folium

# Cordinates of the stadiums
estadios_mexico = {
    "Estadio Azteca (CDMX)": [19.3029, -99.1506],
    "Estadio Akron (Guadalajara)": [20.6755, -103.462],
    "Estadio BBVA (Monterrey)": [25.6687, -100.3116]
}

# Cordinates of the breweries
plantas_cerveza = {
    "Planta Grupo Modelo (CDMX)": [19.4401, -99.1255],
    "Planta Heineken (Monterrey)": [25.7304, -100.3147],
    "Planta Grupo Modelo (Guadalajara)": [20.725, -103.3307]
}

# Asign a supply chain to each stadium
abastecimiento = {
    "Estadio Azteca (CDMX)": ["Planta Grupo Modelo (CDMX)"],
    "Estadio Akron (Guadalajara)": ["Planta Grupo Modelo (Guadalajara)"],
    "Estadio BBVA (Monterrey)": ["Planta Heineken (Monterrey)"]
}

# Create a map centered in Mexico
mapa_mexico = folium.Map(location=[23.6345, -102.5528], zoom_start=5)

# Colour code for the breweries
colores = {
    "Planta Grupo Modelo (CDMX)": "green",
    "Planta Heineken (Monterrey)": "red",
    "Planta Grupo Modelo (Guadalajara)": "purple"
}

# Add markers for the stadiums
for estadio, coords in estadios_mexico.items():
    folium.Marker(
        location=coords,
        popup=estadio,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(mapa_mexico)

# Add markers for the breweries
for planta, coords in plantas_cerveza.items():
    folium.Marker(
        location=coords,
        popup=planta,
        icon=folium.Icon(color=colores[planta], icon="industry")
    ).add_to(mapa_mexico)

# Guardar el mapa en un archivo HTML
mapa_mexico.save("../images/mapa_estadios_plantas_cerveza_mundial_2026_mexico.html")

print("Mapa guardado como 'mapa_estadios_plantas_cerveza_mundial_2026_mexico.html'")
