#Refrences
#Bernard Piette and Kasper Peeters; Durham University; 2022

import numpy as np
import matplotlib.pyplot as plt 
import covid19

dmax = 60 # The number of days to use for the integration
cov = covid19.Covid(Rpar=1.71, Kf=0.01, Pop=209e6)  # Set the model parameters, UK

# Set the initial condition and the maximum length of integrationnumber of
cov.initialise(days=dmax, I0=16000) 

# Read the experimetal data from a file
cov.read_data("data_BR_tot.txt", "Brazil")

# Plot the probability distributions
#cov.plot_probabilities()

# Integrate the equations for the specific duration
cov.iterate(dmax)

# Generate figures
cov.plot()
