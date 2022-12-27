#Refrences
#Bernard Piette and Kasper Peeters; Durham University; 2022

import numpy as np
from lin_regression import fit
#from lin_regression_test import fit

def read_data(fname):
   """
   Read a CSV file with lines formatted as
      date, cases, deaths 
   and return just the latter two.

   Args:
      fname: Filename of the CSV file.      

   Returns:
      A list of lists, [cases, fatalities].

   """
   cases = []
   fatalities = []
   fp = open(fname)
   for line in fp:
       s = line.split() # DATE, CASES, DEATHS
       cases.append( int(s[1]) )
       fatalities.append( int(s[2]) )
   return [cases, fatalities]

def print_result(r):
   """
   Output the result of the `fit` function in a
   nicely formatted form.
   """
   print("Country:", r[0])
   print("  A             =", r[1])
   print("  lamda         =", r[2])
   print("  doubling time =", r[3])
   d=6.5
   R=np.exp(r[2]*(d+1))
   print("  R             =", R)

   
fname_uk = "data_UK_tot.txt"
fatalities_uk = read_data(fname_uk)[1]
print_result( fit(fatalities_uk, dmin=35, dmax=65, country="UK") )

fname_brazil = "data_BR_tot.txt"
fatalities_brazil = read_data(fname_brazil)[1]


print_result( fit(fatalities_brazil, dmin=35, dmax=65, country="Brazil") )
