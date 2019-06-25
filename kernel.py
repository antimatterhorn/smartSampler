import numpy as np
from math import *

def W(r,h):
	r = abs(r) #protection
	a = 10.0/(7.0*np.pi*h**2)
	if r>= 2.0:
		return 0
	elif r>=1.0:
		return a*0.25*(2.0-r)**3
	else:
		return a*(1.0-1.5*r**2+0.75*r**3)

def gradW(r,h):
	return 0.