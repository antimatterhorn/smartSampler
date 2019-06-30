import numpy as np
from math import *

def W(e,h):
	e = abs(e) #protection
	a = 10.0/(7.0*np.pi*h**2)
	#a = 1.0/(np.pi*h**3)
	if e>= 2.0:
		return 0
	elif e>=1.0:
		return a*0.25*(2.0-e)**3
	else:
		return a*(1.0-1.5*e**2+0.75*e**3)

def gradW(e,h):
	return 0.