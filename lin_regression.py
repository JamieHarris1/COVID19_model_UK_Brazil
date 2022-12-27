import numpy as np
import matplotlib.pyplot as plt 
import scipy.optimize

def fit(data, dmin, dmax, country):

    def log_func(x, a, b):
        f = np.log(a) + b*x
        return f
    
    def func(x, a, b):
        f= a * np.exp(b * x)
        return f
    
    #days between dmax and dmin exluding last one
    days=np.linspace(dmin, dmax - 1, dmax - dmin).astype(np.int64)  

    #only want data over days dmin to dmax 
    data = data[dmin:dmax]    

    #fitting log function to log of data
    popt, pcov = scipy.optimize.curve_fit(log_func, days, np.log(data))  

    plt.xlabel("Days", fontsize=22)
    plt.ylabel("Fatalities", fontsize=22)
    plt.xticks(fontsize=20) # Makes x labels digits larger
    plt.yticks(fontsize=20) # Makes y labels digits larger
    plt.tight_layout(rect=[0, 0, 1, 1]) # Ensure the full figure is visible
    plt.title(country,fontsize=22)

    plt.semilogy(days, data, "b*") # Plot data
    plt.semilogy(days, func(days, *popt), 'r--')
    #plt.savefig("Exponential_Fit_{}.pdf".format(country))
    plt.show()

    A = popt[0]
    lamb = popt[1]
    dt = np.log(2) / lamb
    return (country, A, lamb, dt)