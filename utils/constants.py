from typing import List 
from dataclasses import dataclass

@dataclass
class UkParams:
    country: str = 'UK'
    pop: int = 66e6

    tmax: int = 150     #number days to simulate over
    d: int = 7          #number of days infectious then recover/die
    Rpar = 4.6            #average number of additional people an infected person will infect  
    Kf: float = 0.01   #fatality probability
    
    #range for linear regression params to be calculated over
    dmin: int = 35      
    dmax: int = 60

    I0: int = 2
    
@dataclass
class BrazilParams:
    country: str = 'BR'
    pop: int = 209e6

    tmax: int = 150     #number days to simulate over
    d: int = 7          #number of days infectious then recover/die
    Rpar = 1.71            #average number of additional people an infected person will infect  
    Kf: float = 0.01   #fatality probability
    
    #range for linear regression params to be calculated over
    dmin: int = 35      
    dmax: int = 60

    I0: int = 16000

