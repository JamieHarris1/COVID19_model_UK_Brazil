import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy.optimize
from utils.constants import UkParams as cs

class LinearRegression:
    def __init__(self, data: pd.DataFrame, country: str, column_name: str, dmin: int, dmax: int):
        self.country = country
        self.column_name = column_name
        self.dmin = dmin
        self.dmax = dmax
        self.data = data[self.dmin:self.dmax]
        self.days = np.linspace(self.dmin, self.dmax, self.dmax - self.dmin).astype(np.int64)

    @staticmethod
    def log_func(t: pd.DataFrame, a: float, b: float):
        f = np.log(a) + b*t
        return f

    @staticmethod
    def func(t: pd.DataFrame, a: float, b: float):
        f = a * np.exp(b * t)
        return f
    
    def fit(self):
        popt, pcov = scipy.optimize.curve_fit(
            LinearRegression.log_func, self.data['Day'], np.log(self.data[self.column_name])
        )  
        print(popt)
        A = popt[0]
        lamb = popt[1]
        return A, lamb

    def plot_fit(self, A: float, lamb: float):
        plt.xlabel("Days", fontsize=22)
        plt.ylabel("Fatalities", fontsize=22)
        plt.xticks(fontsize=20) # Makes x labels digits larger
        plt.yticks(fontsize=20) # Makes y labels digits larger
        plt.tight_layout(rect=[0, 0, 1, 1]) # Ensure the full figure is visible
        plt.title(self.country,fontsize=22)

        plt.semilogy(self.data['Day'], self.data[self.column_name], "b*") # Plot data
        plt.semilogy(self.data['Day'], LinearRegression.func(self.data['Day'], A, lamb), 'r--')
        #plt.savefig("Exponential_Fit_{}.pdf".format(country))
        plt.show()

    def print_result(self, A: float, lamb: float):
        tau = np.log(2) / lamb
        R=np.exp(lamb*(cs.d+1))
        print(f'''
            Country:        {self.country}
            A:              {A}
            lambda:         {lamb}
            doubling time:  {tau}
            R:              {R}
            ''')
    