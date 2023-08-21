import numpy as np
import matplotlib.pyplot as plt 
from covid19_model import covid19
from utils.data import Data
# from utils.constants import UkParams as cs
from utils.constants import BrazilParams as cs

# Set the model parameters, UK
cov = covid19.Covid(Rpar=cs.Rpar, Kf=cs.Kf, Pop=cs.pop, days=cs.dmax, I0=cs.I0, country=cs.country)  

# Read the experimetal data from a file
cov.data = Data.load_data(f"utils/data_{cs.country}_tot.csv")

# Plot the probability distributions
cov.plot_probabilities()

# Interrate the population for the sepcified number of days
for d in range(0, cs.dmax):
	cov.step(d)

# Generate figures
cov.plot(data_c=False, data_f=True)
