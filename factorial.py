def factorial(x):
	y=1
	for i in range(x):
		y = y * (i + 1)
	return y

print (factorial(4))
