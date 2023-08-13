import matplotlib.pyplot as plt
from utils.constants import Params as cs

class Covid19:
	def __init__(self):
		self.S = [66e6]  #UK population
		self.I = [1]     #infections
		self.R = [0]     #recoveries
		self.F = [0]     #fatalities
		self.DI = [0]*cs.d + [self.I[-1]]
		self.Pop = self.S[-1] + self.I[-1] + self.R[-1]
		self.K: float = cs.Rpar/cs.d

	def plot(self):
		plt.semilogy(self.I,"r*", label="I")
		plt.semilogy(self.R,"b*", label="R")
		plt.semilogy(self.F,"k*", label="F")
		plt.xlabel("i", fontsize=30)
		plt.ylabel("I/R/F", fontsize=30)
		plt.legend(loc='lower left',prop={'size': 20})
		plt.tight_layout(rect=[0, 0, 0.99, 1], pad=0.5)
		#plt.savefig("SIR_R{}_tmax{}.pdf".format(Rpar,tmax))
		plt.show()

	def main(self):
		for i in range(cs.tmax):
			DeltaI = self.K*self.S[-1]*self.I[-1]/self.Pop
			self.S.append(self.S[-1]-DeltaI)
			self.I.append(self.I[-1]+DeltaI-self.DI[-cs.d])
			self.R.append(self.R[-1]+(1-cs.Kf)*self.DI[-cs.d])
			self.F.append(self.F[-1]+cs.Kf*self.DI[-cs.d])
			self.DI.append(DeltaI)
			# print(Pop)  #population for each time period, showing it is constant
		Covid19.plot(self)
		print("I={} R={} F={}".format(self.I[-1], self.R[-1], self.F[-1]))

if __name__ == '__main__':
	covid_sim = Covid19()
	covid_sim.main()