# flow_analysis.py
class FlowAnalysis:
    def __init__(self, supply_network):
        self.network = supply_network

    def analyze_flow_distribution(self):
        for edge in self.network.graph.edges(data=True):
            print(f"Flow on edge {edge}: {edge[2]['capacity']} units")

    def simulate_demand(self, demand_variation):
        print(f"Simulating demand variation: {demand_variation}")
        # Code to adjust flow and demand as needed
