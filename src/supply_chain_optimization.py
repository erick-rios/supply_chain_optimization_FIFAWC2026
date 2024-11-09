!pip install pulp

import pandas as pd
from pulp import *

# Import data of costs
manufacturing_costs = pd.read_csv("../data/variable_costs.csv")
manufacturing_costs

# Import data of costs
freight_costs = pd.read_csv("../data/freight_costs.csv")
freight_costs

