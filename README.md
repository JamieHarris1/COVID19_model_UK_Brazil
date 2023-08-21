# COVID19_model_UK_Brazil

Program to implement a various mathematical models for COVID19 in the Uk and Brazil

### SIR model

- Divide people into 4 categories: Susceptible, Infected, Recovered, Dead
- Use recurrence relations to model the population over discrete intervals
  ![Screenshot](screenshots/screenshot.png)

### Linear regression model to estimate R parameter

- Pandemic can be seen to follow an exponential relationship at the begining of the pandemic
- Use linear regression to estimate this parameter

### Gamma prior model

- Assume prior distributions for key metrics instead of constants
- e.g The probability of infefcting someone else or recovering after being infected for d days
