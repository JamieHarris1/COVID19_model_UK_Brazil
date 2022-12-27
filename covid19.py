import numpy as np
import matplotlib.pyplot as plt 
from covid19_base import *

class Covid(Covid_base):

    def step(self): # Perform a single integration step

        """ Perform a single integration step of the SIR model for Covid 19
        """
        
        
        def expected_var(prob_array):
            #limits DI array to number of previous days needed for calcluation
            dummy_DI = self.DI[self.pad + self.d - len(prob_array) + 1:self.pad + self.d + 1] 

            #finds sum of expected values over length of prob_array days
            expected_var = np.dot(dummy_DI, prob_array[::-1])
            return expected_var
        
        DI = expected_var(self.Pi)
        self.DI[self.d+self.pad] = self.Rpar*DI*self.S[self.d]/self.Pop
        Drd=expected_var(self.Pr)
        
        
        

        self.DR[self.d] = (1 - self.Kf) * Drd
        self.DF[self.d] = self.Kf * Drd
        self.S[self.d + 1] = self.S[self.d] - self.DI[self.pad + self.d]
        self.I[self.d + 1] = self.I[self.d] + self.DI[self.pad + self.d] \
                           - self.DR[self.d] - self.DF[self.d]
        self.R[self.d+1] = self.R[self.d] + self.DR[self.d]
        self.F[self.d+1] = self.F[self.d] + self.DF[self.d] 
    
        
        
        
       
