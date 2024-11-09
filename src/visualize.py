!pip install folium

import folium

# Coordinates of the Mexican stadiums to be used in the 2026 World Cup
estadios_mexico = {
    "Estadio Azteca (CDMX)": [19.3029, -99.1506],
    "Estadio Akron (Guadalajara)": [20.6755, -103.462],
    "Estadio BBVA (Monterrey)": [25.6687, -100.3116]
}

# Crear a map centered in Mexico
mapa_mexico = folium.Map(location=[23.6345, -102.5528], zoom_start=5)

# Add a marker for each stadium
for estadio, coords in estadios_mexico.items():
    folium.Marker(
        location=coords,
        popup=estadio,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(mapa_mexico)

# Save maps as HTML file
mapa_mexico.save("../images/mapa_estadios_mundial_2026_mexico.html")

print("Mapa guardado como 'mapa_estadios_mundial_2026_mexico.html'")
