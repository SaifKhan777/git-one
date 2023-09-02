# pip install pgmpy (different cell or in cmd prompt)

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create a Bayesian Network model
model = BayesianNetwork([('A', 'C'), ('B', 'C')])

# Define Conditional Probability Distributions (CPDs)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_c = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.8, 0.9, 0.7, 0.1], [0.2, 0.1, 0.3, 0.9]],
                   evidence=['A', 'B'],
                   evidence_card=[2, 2])

# Add CPDs to the model
model.add_cpds(cpd_a, cpd_b, cpd_c)

# Check model for consistency
assert model.check_model()

# Create an inference object
inference = VariableElimination(model)

# Calculate probabilities
result = inference.query(variables=['C'], evidence={'A': 1, 'B': 0})
print(result)
