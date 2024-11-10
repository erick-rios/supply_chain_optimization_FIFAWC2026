# resilience_simulation.py
import random

class ResilienceSimulation:
    def __init__(self, supply_network):
        self.network = supply_network

    def simulate_failure(self, num_failures=1):
        failed_nodes = random.sample(self.network.graph.nodes(), num_failures)
        print(f"Simulating failures at nodes: {failed_nodes}")
        self.network.graph.remove_nodes_from(failed_nodes)
