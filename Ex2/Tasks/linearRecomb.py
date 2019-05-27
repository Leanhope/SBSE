import numpy as np
import random

def main():

	p = 0.25
	n= 6
	x = [round(random.random()*5, 2) for _ in range(n)]
	v = [round(random.random()*5, 2) for _ in range(n)]
	alpha = round(np.random.uniform(-p, 1+p), 2)
	beta = round(np.random.uniform(-p, 1+p), 2)

	print("alpha: ", alpha)
	print("beta ", beta)
	print("X: ", x)
	print("V: ", v)

	for i in range(0, len(x)):
		t = round(alpha*x[i] + (1-alpha)*v[i], 2)
		s = round(beta*v[i] + (1-beta)*x[i], 2)

		#Sind die bounds richtig?
		if min(t, s) >= (min(x[i], v[i])-p) and max(t, s) <= (max(x[i], v[i])+p):
			x[i] = t
			v[i] = s
			
	print("X': ",x)
	print("V': ",v)

if __name__ == '__main__':
	main()
	