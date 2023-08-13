import numpy as np
import pandas as pd
from utils.data import Data
from utils.constants import Params as cs
from linear_regression.functions import LinearRegression

class Run:
	@staticmethod
	def start():
		uk_data = Data.load_data(f"utils/data_{cs.country}_tot.csv")
		lin_reg = LinearRegression(uk_data, cs.country, 'Fatalities', dmin=cs.dmin, dmax = cs.dmax)
		A, lamb = lin_reg.fit()
		lin_reg.print_result(A, lamb)
		lin_reg.plot_fit(A, lamb)

if __name__ == '__main__':
	Run.start()


