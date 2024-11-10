# cost_optimization.py
#!pip install pyomo

from pyomo.environ import *

class CostOptimization:
    def __init__(self, supply_network):
        self.model = ConcreteModel()
        self.network = supply_network

    def create_model(self):
        nodes = list(self.network.graph.nodes())
        edges = list(self.network.graph.edges())

        # Variables: flow on each edge
        self.model.flow = Var(edges, within=NonNegativeReals)

        # Objective function: Minimize total cost
        self.model.obj = Objective(
            expr=sum(self.model.flow[e] * self.network.graph[e[0]][e[1]]['cost'] for e in edges),
            sense=minimize
        )

        # Capacity constraints
        def capacity_constraint(model, i, j):
            return model.flow[i, j] <= self.network.graph[i][j]['capacity']

        self.model.constraints = Constraint(edges, rule=capacity_constraint)

    def solve(self):
        solver = SolverFactory('glpk')
        result = solver.solve(self.model)
        return result
