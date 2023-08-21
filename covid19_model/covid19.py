import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import gamma

class Covid():
    def __init__(self, Rpar, Kf, Pop, days, I0, country):
        """ 
           : param Rpar : infection rate
           : param Kf : Fatality rate
           : param Pop : Total population
        """
        self.Rpar = Rpar 
        self.Kf = Kf 
        self.Pop =  Pop 
        self.days = days
        self.I0 = I0
        self.pad = 60 # padding larger than probabilities length
        self.S = np.zeros(self.days+1) # Susceptible population
        self.DS = np.zeros(self.days+1+self.pad)
        self.I = np.zeros(self.days+1) # Infected population
        self.DI = np.zeros(self.days+1+self.pad) # New infection
        self.R = np.zeros(self.days+1) # Recovered population
        self.DR = np.zeros(self.days+1) # New recovery
        self.F = np.zeros(self.days+1) # Dead population
        self.DF = np.zeros(self.days+1) # New fatalities
        self.S[0] = self.Pop-I0
        self.I[0] = I0
        self.DI[self.pad-1] = I0
        self.d = 0

        # Initiliase the probabilities
        # Imperial : gamma(xi,6.5,0.62)
        xi = np.linspace(0,40,41)
        #prob of being infectious x days after being infected
        self.Pi = self.mk_gamma(xi, 6.5,  0.62, t_pad=0, inv=False)
        # Imperial gamma(18.8,0.45) is from symptoms
        xe = np.linspace(0,60,61)
        self.Pr_sym = self.mk_gamma(xe, 18.8, 0.45, t_pad=0, inv=False)
        # Imperial gamma(5.1,0.0.86) is from symptoms
        xe = np.linspace(0,60,61)
        self.Pinc = self.mk_gamma(xe, 5.1, 0.86, t_pad=0, inv=False)
        
        self.Pr = np.convolve(self.Pinc, self.Pr_sym, mode='full')[0:60]
        self.Pr = self.Pr/sum(self.Pr) # normalise the truncated probability
        #print("SUM Pinc=",sum(self.Pinc))
        #print("SUM Pr_sym=",sum(self.Pr_sym))
        #print("SUM Pr=",sum(self.Pr))
        self.data = []
        self.country = country

    def plot_probabilities(self):
        """ Generate a graph of the probability distributions.
        """
        plt.rc("xtick",labelsize=20)
        plt.rc("ytick",labelsize=20)

        plt.plot(self.Pi)
        plt.xlabel("days", fontsize=22)
        plt.ylabel("P", fontsize=22)
        plt.title(r'$P_{Inf}$', fontsize=22)
        plt.tight_layout(rect=[0, 0, 0.99, 1],pad=0.5)
        plt.savefig("plots/Pi.pdf")
        plt.show()
        
        plt.plot(self.Pr_sym)
        plt.xlabel("days", fontsize=22)
        plt.ylabel("P", fontsize=22)
        plt.title(r'$P_{Sym}$', fontsize=22)
        plt.tight_layout(rect=[0, 0, 0.99, 1],pad=0.5)
        plt.savefig("plots/Pr_sym.pdf")
        plt.show()
        
        plt.plot(self.Pinc)
        plt.xlabel("days", fontsize=22)
        plt.ylabel("P", fontsize=22)
        plt.title(r'$P_{Inc}$', fontsize=22)
        plt.tight_layout(rect=[0, 0, 0.99, 1],pad=0.5)
        plt.savefig("plots/Pinc.pdf")
        plt.show()
        
        plt.plot(self.Pr)
        plt.xlabel("days", fontsize=22)
        plt.ylabel("P", fontsize=22)
        plt.title(r'$P_{R}$', fontsize=22)
        plt.tight_layout(rect=[0, 0, 0.99, 1],pad=0.5)
        plt.savefig("plots/Pr.pdf")
        plt.show()
        
    def step(self):
        """ Perform a single integration step of the SIR model for Covid 19
        """
        DI = 0
        for n in range(1,len(self.Pi)):
            DI += self.DI[self.pad+self.d-n]*self.Pi[n]
        self.DI[self.d+self.pad] = self.Rpar*DI*self.S[self.d]/self.Pop

        Drd = 0
        for n in range(1,len(self.Pr)):
            Drd += self.DI[self.pad+self.d-n]*self.Pr[n]

        self.DR[self.d] = (1-self.Kf)*Drd
        self.DF[self.d] = self.Kf*Drd
        self.S[self.d+1] = self.S[self.d]- self.DI[self.pad+self.d]
        self.I[self.d+1] = self.I[self.d]+ self.DI[self.pad+self.d]\
                           -self.DR[self.d]-self.DF[self.d]
        self.R[self.d+1] = self.R[self.d] + self.DR[self.d]
        self.F[self.d+1] = self.F[self.d] + self.DF[self.d] 
       
    def iterate(self):
        """ Interrate the population for the sepcified number of days
        """
        for d in range(0,self.days):
          #print(d, self.S[d], self.I[d],self.DI[d-1+self.pad] )
          self.d = d
          self.step()

    def plot_data(self, data, fmt, label):
        d,t_data = self.larger_than_one_only(range(len(data)), data)
        plt.semilogy(d,t_data,fmt, label=label)

    def plot(self, data_c=False, data_f=True):
        self.plot_data(self.I[:self.d], "r-", label="I")
        self.plot_data(self.R[:self.d], "b-", label="R")
        self.plot_data(self.F[:self.d], "k-", label="F")


        if(data_c):
            plt.semilogy(self.data['Cases'][:self.d], "r*", label="I data") 
        if(data_f):
            plt.semilogy(self.data['Fatalities'][:self.d], "k*", label="F data") 
        
        plt.xlabel("i", fontsize=22)
        plt.ylabel("I/R/F", fontsize=22)
        plt.legend(loc='upper left',prop={'size': 16})
        plt.title("{}: R={}, I0={}".format(self.country, self.Rpar, self.I[0]),fontsize=30)
        plt.tight_layout(rect=[0, 0, 0.99, 1], pad=0.5)
        plt.savefig("plots/Epidemic_{}_R{}_I0{}.pdf".format(self.country, self.Rpar, self.I[0]))
        plt.show()
        #print(self.I[:self.d])


    def expected_var(self, prob_array):
            #limits DI array to number of previous days needed for calcluation
            dummy_DI = self.DI[self.pad + self.d - len(prob_array) + 1:self.pad + self.d + 1] 

            #finds sum of expected values over length of prob_array days
            expected_var = np.dot(dummy_DI, prob_array[::-1])
            return expected_var
    
    def step(self, d): # Perform a single integration step

        """ Perform a single integration step of the SIR model for Covid 19
        """
        self.d = d
        DI = self.expected_var(self.Pi)
        self.DI[self.d+self.pad] = self.Rpar*DI*self.S[self.d]/self.Pop
        Drd = self.expected_var(self.Pr)
        
        self.DR[self.d] = (1 - self.Kf) * Drd
        self.DF[self.d] = self.Kf * Drd
        self.S[self.d + 1] = self.S[self.d] - self.DI[self.pad + self.d]
        self.I[self.d + 1] = self.I[self.d] + self.DI[self.pad + self.d] \
                           - self.DR[self.d] - self.DF[self.d]
        self.R[self.d+1] = self.R[self.d] + self.DR[self.d]
        self.F[self.d+1] = self.F[self.d] + self.DF[self.d] 
    
    @staticmethod
    def mk_gamma(t, mu, var_coef, t_pad=0, inv = True):
        """ Create and return a varience distribution
            : param t : range of values
            : param mu : average
            : param var_coef : coefficient of variation (=sigma/mu)
            : param t_pad : time delay in days before onset  
            : param inv : inverse array for convolution
        """
        lambda_p = np.sqrt(1/(mu*var_coef**2)) # lambda = alpha/mu=1/(mu V^2)
        alpha_p = mu*lambda_p
        Pi = gamma.pdf(t, alpha_p, 0, 1/lambda_p)
        if(t_pad> 0): # add pad to Pi
            Pi = np.pad(Pi, (t_pad,0) ,'constant')
        if(t_pad< 0): # truncate
            Pi = Pi[-t_pad:] 
        Pi = Pi/sum(Pi) # normalise
        if(inv):
            return(Pi[::-1]) 
        return(Pi) 

    @staticmethod
    def larger_than_one_only(d, val):
        """ return sub list with data larger than 1 only
            : param d : data set
            : param val : threshold value
        """
        nd = []
        nval = []
        for n in range(len(d)):
            if(val[n] >= 1):
                nd.append(d[n])
                nval.append(val[n])
        return(nd,nval)