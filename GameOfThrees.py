# Takes an input number, and performs a series of additions and divisions by three until it reaches 1
# Source: https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

def advance():
	global num
	print(int(num), end = "\t\t")
	
	if num == 1:
		exit(0)
	
	if (num + 1) % 3 == 0:
		num += 1
		print(1)
		
	elif (num - 1) % 3 == 0:
		num -= 1
		print(-1)
		
	else:
		print(0)
	
	num = num / 3
	
	advance()
	

num = int(input())
advance()