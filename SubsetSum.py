numbers = [int(x) for x in input().strip('[').strip(']').split(', ')]

for num in numbers:
	if -num in numbers:
		print('true')
		exit()
		
print(0 in numbers)
