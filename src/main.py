!pip install pyomo
!apt install glpk-utils libglpk-dev
!pip install glpk

!glpsol --version

# main.py
from src.network_model import SupplyNetwork
from src.cost_optimization import CostOptimization
from src.flow_analysis import FlowAnalysis
from src.resilience_simulation import ResilienceSimulation
from src.floyd_algorithm import ShortestPath

# Step 1: Create the network
network = SupplyNetwork()
network.add_node('Factory1', 'Factory')
network.add_node('Warehouse1', 'Warehouse')
network.add_node('Retailer1', 'Retailer')
network.add_edge('Factory1', 'Warehouse1', cost=10, capacity=100)
network.add_edge('Warehouse1', 'Retailer1', cost=5, capacity=80)

network.display_network()

# Step 2: Optimize costs
optimizer = CostOptimization(network)
optimizer.create_model()
result = optimizer.solve()
print("Optimization result:", result)

# Step 3: Analyze flow distribution
flow_analysis = FlowAnalysis(network)
flow_analysis.analyze_flow_distribution()

# Step 4: Find shortest paths
shortest_path_finder = ShortestPath(network)
shortest_path_finder.find_all_pairs_shortest_path()

# Step 5: Simulate network resilience
resilience_sim = ResilienceSimulation(network)
resilience_sim.simulate_failure(num_failures=1)
