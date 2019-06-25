
def protect(x):
	if abs(x) < 1e-10:
		x = 1e-10
	return x

def func(xa):
	for i in range(len(xa)):
		xa[i] = protect(xa[i])
	y1=y2=0
	if len(xa)==2:
		y1 = xa[0]**1.1
		y2 = xa[1]**1.3
	return y1,y2