#Refrences
#Bernard Piette and Kasper Peeters; Durham University; 2022

import matplotlib.pyplot as plt

tmax=150
d = 7
Rpar = 1 # R is used below for the recovered population
K= Rpar/d
Kd=0.01
S = [66e6]
I = [1]
R = [0]
F = [0]
DI = [0]*d + [I[-1]]
Pop=S[-1] + I[-1] + R[-1]

for i in range(tmax):
  DeltaI = K*S[-1]*I[-1]/Pop
  S.append(S[-1]-DeltaI)
  I.append(I[-1]+DeltaI-DI[-d])
  R.append(R[-1]+(1-Kd)*DI[-d])
  F.append(F[-1]+Kd*DI[-d])
  DI.append(DeltaI)
  #print(Pop)  #population for each time period, showing it is constant

plt.plot(I,"r*", label="I")
plt.plot(R,"b*", label="R")
plt.plot(F,"k*", label="F")
plt.xlabel("i", fontsize=22)
plt.ylabel("I/R/F", fontsize=22)
plt.legend(loc='upper left')
plt.tight_layout(rect=[0, 0, 0.99, 1], pad=0.5)
plt.show()
print("I={} R={} F={}".format(I[-1],R[-1], F[-1]))
