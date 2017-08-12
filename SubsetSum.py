# Determines whether there exists a pair of numbers in a list that add up to 0 (including 0).
# Challenge: https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/

numbers = [int(x) for x in input().strip('[').strip(']').split(', ')]

for num in numbers:
	if -num in numbers:
		print('true')
		exit()
		
print(0 in numbers)
