xjfg44

Methods in Modelling Covid 19 for both the UK and

Brazil

Abstract

We will look at different methods to model the Covid 19 pandemic in both Brazil and the UK. Initially using a recurrence relation illustrating how different groups within the population as a whole evolve over time. We can then add complexity to our model removing assumptions previously made. Our model can then be calibrated to each of the countries in question separately based on their observed data. This will allow us to observe and compare the difference in key statistics such as the R value defined as the average number of additional people an infected person will infect between our countries in question. The UK imposed strict lockdown rules, in contrast Brazil implemented little to no intervention providing us with a clear comparison.

1  Introduction

Covid 19 was a worldwide pandemic beginning in 2020 encompassing the spread of the disease known as Coronavirus causing severe acute respiratory syndrome[1]. [C](#_page7_x70.87_y203.09)ountries around the world faced an enormous challenge aiming to curb the spread of the disease preventing it running rampant through the population owing to the disease’s high infection rate and estimated fatality rate of 1%[2[\].](#_page7_x70.87_y224.42) Designing a model to forecast cases and fatalities over time is paramount to allow governments to make informed decisions about the welfare of their citizens.

2  Simple SIR model

During the pandemic the evolution of the population can be distilled down into four different states. susceptible: those who have not been infected yet; infectious: those who are ill and infectious and then recovered or fatalities i.e. those who have recovered or those who haven’t.

Recover (R) Susceptible![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.001.png) (S)~~ Infected (I)![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.002.png)

Fatality (F)

Initially we can make a couple assumptions omitting specific factors affecting infection rate such as duration and conditions of interactions between people and how easily the virus can be transmitted. By looking at each day i separately we can create a recurrence relationship for S, I, R and F values on day i dependent on the days before. ∆Ii, the numeber of people infected on any given day i can be described as proportional to the number of susceptible people times the probability a given person is infectious. (Ii/N). d can be described as the number of days a person is infectious before they either recover or die.

∆<a name="_page0_x255.06_y678.02"></a>Ii = KSiIi/N

Si+1 = Si − ∆Ii (1) The Constant K in (1[) can](#_page0_x255.06_y678.02) be described by the following equation:

K = R/d (2)

As mentioned above R is the average number of additional people an infected person will infect and is different from country to country. The fatality rate can be written as Kf allowing us to express the number of people who have been infected, recovered and died on day i+1.

<a name="_page1_x228.08_y133.43"></a>Ii+1 = Ii + ∆Ii − ∆Ii−d

Ri+1 = Ri + (1 − Kf )∆Ii−d

Fi+1 = Fi + Kf ∆Ii−d. (3)

Q1 ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.003.png)The population N can be seen to remain constant as shown below:

Proof.

Ni = Si + Ii + Ri + Fi

- (Si+1 + ∆Ii) + (Ii+1 − ∆Ii + ∆Ii−d) + (Ri+1 − (1 − Kf )∆Ii−d) + (Fi+1 − Kf Ii−d)
- Si+1 + Ii+1 + Ri+1 + Fi+1 (4)

Therefore Ni must be constant for all i ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.004.png)

Q2![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.005.png)

Using our new recurrence relationships we can now model infections for a general country’s recoveries and fatalities against time i for different R values. We will use a log linear graph as it makes it easier to read the data.

101 106![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.006.png)

100 10

3

I I 10 1 R 0 R

10

F F 10 2

0 50 100 150 0 50 100 150

i i

<a name="_page1_x70.87_y392.31"></a>(a) R = 1 (b) R = 2

105

101

10 3 I

R 10 7 F

0 50 100 150 i

(c) R = 3

Figure 1: Modelling different R values

From the graphs above we can infer that the higher the R value the greater the number of total fatalities and concurrent infections. Looking at figure 1a [R=1,](#_page1_x70.87_y392.31) we can observe that infected persons remains constant over time due to straight flat red line. This makes sense as ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.007.png)each person is only infecting one other on average so it is difficult for disease to spread through the population. For greater values of R such as 2 and 3 the number of infections increases exponentially until the proportion of people left to infect is too small no matter the R rate. This can be described by the term herd immunity where the a significant proportion of the remaining population has recovered and is no longer susceptible to the disease causing the rate of new infections to fall. 

3  Exponential Model

At the onset of the pandemic the number of people infected is extremely small in comparison to the total population. As a result we can assume for the first d days S is constant and equal to N, using this simplification (1[) reduces](#_page0_x255.06_y678.02) down to:

Ii+1 = Ii + ∆Ii (5) Moreover, again similarly we can assume recoveries are negligible considering only the first

d days of the pandemic resulting in the following equation for Ii+1:

I<a name="_page2_x230.49_y328.53"></a>i+1 = Ii + R(Ii−d − Ii−d−1) (6)

From figure: [1b ](#_page1_x70.87_y392.31)we can see that initially the infections and fatalities can be seem to be exponentially increasing. As a result we can aim to model this using an exponential distribution of the following form.

I<a name="_page2_x258.66_y403.37"></a>i = Aexp(λi)

Fi = Aexp(λi) (7)

Q4 ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.008.png)Substituting in 7[ in](#_page2_x258.66_y403.37)to 6[ w](#_page2_x230.49_y328.53)e can derive an expression for R in terms of λ and d.

Aexp(λ(i + 1)) = Aexp(λi) + R(Aexp(λ(i − d)) − Aexp(λ(i − d − 1)))

eλeλi = eλi + R(eλie−dλ − eλieλ(−d−1))

eλ = 1 + R(e−dλ − e−λ(d+1))

eλ(eλ − 1)

R =

e−dλ(eλ − 1)

- exp(λ(d + 1)) (8)

Similarly, another parameter epidemiologists use is the doubling time defined as the time for

the number of fatalities or cases to double. We can derive this value τ using our exponential model for the begining of the pandemic.

F<a name="_page2_x226.28_y635.71"></a> = Aexp(λt)

2F = Aexp(λ(t + τ)) = 2Aexp(λt)

λ(t + τ) = log(2) + λt

log2

τ = (9)

λ

Using a separate program and the function 7 [to ](#_page2_x258.66_y403.37)model the data we can use our fatalities data and formula [9 ](#_page2_x226.28_y635.71)to find λ and τ for both equations. We do this as the observed fatality data is more reliable than for cases. The fitting will be performed using the log of the data generating a log linear graph of fatalities against days for both countries assuming d=6.5.

[^1]10[^2] ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.009.png)![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.010.png)![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.011.png)

103 101 

103 

40 50 60 40 50 60 

Days Days 

(a) UK (b) Brazil 

Figure 2: Fitting exp model to fatalities data 



|Country|λ|Doubling time|R|A|
| - | - | - | - | - |
|UK|0\.294|2\.35|9\.10|6\.69e-5|
|Brazil|0\.0793|8\.74|1\.81|71\.3|

It can be seen above that UK had a significantly larger R value suggesting the infection ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.012.png)spread much more rapidly than in Brazil initially. In addition, the shorter doubling time for fatalities supports this conclusion as infections directly lead to fatalities. 

4  More general SIR Model

A more general model still consists of the same four stages as mentioned above depending

on time d when initially exposed although now once you are exposed to the virus you are not infectious for a few days. After they can then contaminate others and will ultimately recover

or not. In our model we will not look at displaying symptoms as an informative state as many people with Covid 19 do not display symptoms but are still infectious. However, now we will introduce the probability distributions to further our model. The probability to be infected on

day d will be proportional to the probability to meet someone who was infected on day d − 1 times the respective probability, PInf that a person is infectious after 1 day, plus the probability

that they were infected on day d − 2 times the probability of infection after 2 days, plus ...

This can be summarised but the following equation.

∆Ii = RSi Ni ∆Ii−dPInf (d) (10)

N

d=1

where ni is the number of days such that PInf (d) = 0 if d > ni. The distribution of fatalities and recoveries are shown to be similar in [3][ as](#_page7_x70.87_y273.57) a result define this probability distribution as Pr(d) for both.

<a name="_page3_x216.67_y654.01"></a>nr

∆Fi = Kf ∆Ii−dPr(d)

d=1

nr

∆Ri = (1 − Kf ) ∆Ii−dPr(d) (11)

d=1

PInf = Gamma(6.5,0.62) PInc = Gamma(5.1,0.86) PR = Gamma(18.8,0.45)

5
xjfg44

PInf![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.013.png)

0\.10 0.05 0.00

0 10 20 30 40

days

1) PInf

PInc

0\.15 0.10 0.05 0.00![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.014.png)

0 20 40 60

days

2) PInc


xjfg44

PR![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.015.png)

0\.06 0.04 0.02 0.00

0 20 40 60

days

3) PR

Figure 3: Modelling different R values

The probability of recovering Pr(d) can be thought of as the sum of all possible combinations

for n days then recovering n-d days later. eg for d=4

d

<a name="_page4_x216.85_y558.67"></a>Pr(d) = PInc(n)PR(d − n) (12)

n=0

Days Incubating Days till recovery after inc 4![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.016.png) 0

3 1

2 2

1 3

0 4

Q3 ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.017.png)By assuming that PInc(d) and PR(d) are 0 outside the domain d[0,N ] for some N, it can be

shown that Pr(d) is 0 for d < 0.

Proof. Using [12 ](#_page4_x216.85_y558.67)![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.018.png)

d 

Pr(d) = PInc(n)PR(d − n) 

n=0 

d < 0 

d ̸∈ [0,N ] 

Pr(d) = PR(d) = PInc = 0 (13) The largest value that d can be such that Pr(d) is non-zero is d = 2N. 

Proof. Pr(d) = 0 when either: 1) PR(d − n) = 0 or 2) PInc(n) = 0 ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.019.png)

1) Zero when d − n > N 

   2) Zero when n > N 

So boundary for both is when n=N, d > 2N 

2N 

Pr(2N) = PInc(n)PR(2N − n) 

n=0 

- PInc(N)PR(N) 

\> 0 (14) 

Since functions PInc(n) or PR(2N − n) are zero for all other values of n. We can also look at 

d = 2N + 1 to check not larger and non-zereo. 

2N +1 

Pr(2N + 1) = PInc(n)PR(2N − n + 1) 

n=0 

N 2N +1 

- PInc(n)PR(2N + 1 − n) + PInc(n)PR(2N − n + 1) 

n=0 n=N +1 

- 0 for all n (15) 

Therefore 2N is largest value d can be such that Pr(d) is non-zero. 

Pr(d) can also be shown to itself be a probability distribution with ∞d=0 Pr(d) = 1 and Pr(d) > 0 for all d. 

Proof. 

∞ ∞ d 

Pr(d) = PInc(n)PR(d − n) 

d=0 d=0 n=0 

2N d ∞ d 

- PInc(n)PR(d − n) + PInc(n)PR(d − n) 

d=0 n=0 d=2N +1 n=0 

2N d 

- PInc(n)PR(d − n) 

d=0 n=0 

2N d 

- PR(d − n) PInc(n) 

d=0 n=0 

- 1 (16) 
5  Results

Q5 ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.020.png)Using the model we have just constructed we can again look at the UK and Brazil to estimate

R but also I0, the assumed initial infections within our model. We can start with the values

estimated by our simpler model earlier, R= 9.10 for the UK and R=1.81 for Brazil. For our

starting I0 values we can use I0 = 1 for the UK and I0 = 10000 for Brazil. Then we can fine

tune these starting values to more accurately fit our data.

UK: R=9.1, I0=1.0 UK: R=4.6, I0=2.0 ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.021.png)![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.022.png)108 108

I I

R R

105 F 105 F

F data F data

102 102

0 20 40 60 0 20 40 60

i i

Figure 4: UK: Fine tune parameters to data

Brazil: R=1.81, I0=10000.0 Brazil: R=1.71, I0=16000.0

I I 105 R 105 R

F F

F data F data

103

102

101

0 20 40 60 0 20 40 60

i i

Figure 5: Brazil: Fine tune parameters to data

Q6 ![](Aspose.Words.c1279777-7168-4737-8b1a-4dc7a766bf02.023.png)The profile of fatalities for the United Kingdom and Brazil are very different. On the

logarithmic plot for the UK it is pretty much a straight line from the onset. This can be

explained by the UK’s implementations of various lockdowns and other curbing measures such

as social distancing and mask wearing. As a result the straight line is produced suggesting the

factors that such herd immunity that curb the exponential distribution never came into effect.

While for Brazil it is curving down owing to the lack of intervention meaning the virus

eventually came to its natural conclusion for our model where either everyone has recovered or

not.

6  Conclusion

In conclusion, our model can be seen to shown the differences and similarities for the Covid 19 pandemic in both the UK and Brazil. Each of our countries had extreme exponential growth

in both cases and fatalities. During the early onset of the pandemic owing to the disease’s high

infection rate R values were high and greater than 1. However, after the initial period the evolution of the pandemic began to diverge between the countries with the UK continuing this

exponential growth seen as a straight line on our log linear graphs. The major reason for this

would be the impact of lockdown rules disrupting the transmission of the disease. In        comparison, in Brazil no counteracting measures were taken so the disease was left to come to its own conclusion whereby herd immunity had been achieved with enough people within the

population having had the disease. This resulted in the fatality and cases curves to tail off and

curve back down. As a result our model performed best at predicting the pandemic in Brazil since our recurrence relation could more accurately describe the evolution of the population overtime without unaccounted for events like lock downs occurring.

References

1. Wikipedia<a name="_page7_x70.87_y203.09"></a> Covid-19 pandemic(2020) h[ttps://en.wikipedia.org/wiki/COVID-19pandemic](https://en.wikipedia.org/wiki/COVID-19_pandemic)
1. Flaxman<a name="_page7_x70.87_y224.42"></a> et. al, Report 13: Estimating the number of infections and the im- pact of non-pharmaceutical interventions on COVID-19 in 11 European countries <https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/>
1. Stephen<a name="_page7_x70.87_y273.57"></a> A. Lauer et. al, The Incubation Period of Coronavirus Disease 2019 (COVID-19) From Publicly Reported Confirmed Cases: Estimation and Application Ann. Intern. Med. doi:10.7326/M20-0504
9

[^1]: Again where nr is the number of days such that Pr(d) = 0 if d > nr. We can now substitute [11 ](#_page3_x216.67_y654.01)into [3 ](#_page1_x228.08_y133.43)to give our general equation. Our Probability distributions can be defined as follows

    argued in [[2\]](#_page7_x70.87_y224.42) and [[3\]](#_page7_x70.87_y273.57)
[^2]: 