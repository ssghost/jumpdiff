import numpy as np
from JumpDiff.formulae import Qratio, jdprocess

def test_fomulae():
    for power in [1,2,3,4,5,6,7,8,9]:

        M_formula(power = power)

        F_formula(power = power)
        
        F_formula_solver(power = power)
