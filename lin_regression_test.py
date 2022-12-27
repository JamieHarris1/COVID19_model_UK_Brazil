#Refrences
#Bernard Piette and Kasper Peeters; Durham University; 2022

import numpy as np
import matplotlib.pyplot as plt 
import scipy.optimize

def fit(data, dmin, dmax, country):
    # TO COMPLETE
    def log_func(x, a, b):
        f=np.log(a) + b*x
        return f
    
    def func(x,a,b):
        f= a * np.exp(b*x)
        return f
    
    days=np.linspace(dmin, dmax - 1, dmax - dmin).astype(np.int64)   #days between dmax and dmin exluding last one
    data = data[dmin:dmax]    #only want data over days dmin to dmax


    popt, pcov = scipy.optimize.curve_fit(func, days, data)

    plt.xlabel("Days", fontsize=22)
    plt.ylabel("Fatalities", fontsize=22)
    plt.xticks(fontsize=20) # Makes x labels digits larger
    plt.yticks(fontsize=20) # Makes y labels digits larger
    plt.tight_layout(rect=[0, 0, 1, 1]) # Ensure the full figure is visible

    plt.semilogy(days, data, "b*") # Plot data
    plt.semilogy(days, log_func(np.log(days), *popt), 'r--', label="fit to N(t) = k / (kbe−rt + 1)")
    plt.show()

