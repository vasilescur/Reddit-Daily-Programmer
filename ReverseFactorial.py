# Computes the reverse factorial of a number (Ex. "24" --> "4!")
# Source: https://www.reddit.com/r/dailyprogrammer/comments/55nior/20161003_challenge_286_easy_reverse_factorial/

import math

orig = int(input("Number: "))

for x in range(1, int(math.ceil(math.sqrt(orig)))):
	if math.factorial(x) == orig:
		print(str(orig) + " = " + str(x) + "!")
		exit(0)

print("None")
