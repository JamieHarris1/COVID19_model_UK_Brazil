from typing import List 
from dataclasses import dataclass

@dataclass
class Params:
    country: str = 'UK'
    # country: str = 'BR'

    tmax: int = 150     #number days to simulate over
    d: int = 7          #number of days infectious then recover/die
    Rpar = 3            #average number of additional people an infected person will infect  
    Kf: float = 0.103   #fatality probability
    
    #range for linear regression params to be calculated over
    dmin: int = 35      
    dmax: int = 65
