import numpy as np
import random

def main():

	n = 10

	x = [_ for _ in range(n)]
	v = [round(random.random()*100, 2) for _ in range(n)]

	for i in range(1, len(v)):
		v[i] = round(v[i - 1] + v[i], 2)

	p = []

	index = 0
	counter = 0
	s = v[len(v)-1]
	print("X: ", x)
	print("V: ", v)
	print("Sum: ", s)
	offset = round((random.random() * 100) % (s/len(x)), 2)
	print("Offset: ", offset)
	print("StepSize: ", round((s/len(x)), 2))

	points = [round(offset + i * (s/len(x)), 2) for i in range(len(x))]

	print("Points: ", points)

	for point in points:
		while v[index] < point:
			index = index + 1
		p.append(x[index])
	print("Chosen parents: ", p)

if __name__ == '__main__':
    main()
