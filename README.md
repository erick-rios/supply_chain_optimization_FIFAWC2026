# Beer Supply Chain Route Optimization in Mexico

This project is designed to optimize beer supply to the stadiums hosting the FIFA World Cup 2026 in Mexico. It leverages Dijkstra's algorithm to find the shortest paths between nodes in a network comprising breweries, distributors, and stadiums.

![Network Map Preview](images/Screenshot%202024-11-18%20at%2014-53-23%20.png)


## Table of Contents

1. [Description](#description)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Visualization](#visualization)

9. [License](#license)

## Description

The main objective is to build an efficient tool to calculate optimal routes and generate an interactive map visualizing the supply network. The nodes are categorized as follows:
- **Stadiums:** Represented in orange.
- **Distributors:** Represented in blue.
- **Breweries:** Represented in green.

## Project Structure

```plaintext
.
├── data
│   └── network_info.json       # JSON file with network data
├── images                      # Directory for generated images
├── network_map.html            # Generated interactive map
├── README.md                   # This file
├── src
│   ├── app.py                  # Main application entry point
│   ├── dijkstra.py             # Dijkstra's algorithm implementation
│   ├── heapq.py                # MinHeap implementation
│   ├── __init__.py             # Module initializer
│   ├── main.py                 # Script to run the application from the console
│   ├── network_model.py        # Model for handling the network
│   └── visualize.py            # Visualization with Folium
└── test
    ├── __init__.py             # Test module initializer
    └── test.py                 # Unit tests for key functions
```

## Prerequisite

- Python 3.9 or later
- Python libraries:
    - folium
    - networkx
    - json

Install the dependencies with 

```bash
pip install -r requirements.txt
```

## Installation

- **Clone this repository:**
```bash
git clone https://github.com/erick-rios/supply_chain_optimization_FIFAWC2026/
```
- **Navigate to the project directory:**
```bash
cd route-optimization
```
- **Install the dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

- Ensure the `netwokr_info.json` file is in the `data/` directory with the network details
- Run the main script `main.py` using the following command:
```bash
python -m src.main data/network_info.json <start_node> <end_node>
```
- For example:
```bash
python src/main.py data/network_info.json "Planta_Budweiser" "Azteca Stadium"
```
- The interactive map will be saved as `network_map.html`in the root directory.

## Visualization

The file `network_map.html` contains an interactive map generated with `folium`. Open this file in your browser to explore the network and its connections.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

