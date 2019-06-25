
def protect(x):
	if abs(x) < 1e-10:
		x = 1e-10
	return x

def func(xa):
	x1 = protect(xa[0])
	x2 = protect(xa[1])
	x3 = protect(xa[2])
	x4 = protect(xa[3])
	y1 = (x1**0.3) + (x2**0.3) - (x3**1.5/x4**0.2)
	y2 = (x1**1.1/x2**0.2) - x3**1.2 + x4
	return y1,y2