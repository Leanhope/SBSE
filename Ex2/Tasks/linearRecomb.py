import numpy as np
import random

p = 0.25
x = [random.random()*5 for _ in range(6)]
v = [random.random()*5 for _ in range(6)]
alpha = np.random.uniform(-p, 1+p)
beta = np.random.uniform(-p, 1+p)

print("alpha: ", alpha)
print("beta ", beta)
print("X: ", x)
print("V: ", v)

for i in range(0, len(x)):
	t = alpha*x[i] + (1-alpha)*v[i]
	s = beta*v[i] + (1-beta)*x[i]

	#Sind die bounds richtig?
	if min(t, s) >= (min(x[i], v[i])-p) and max(t, s) <= (max(x[i], v[i])+p):
		x[i] = t
		v[i] = s
		
print("X': ",x)
print("V': ",v)
