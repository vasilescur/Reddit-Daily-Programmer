import math

orig = int(input("Number: "))

for x in range(1, int(math.ceil(math.sqrt(orig)))):
	if math.factorial(x) == orig:
		print(str(orig) + " = " + str(x) + "!")
		exit(0)

print("None")
