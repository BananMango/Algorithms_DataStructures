# https://www.e-olymp.com/ru/contests/15266/problems/155829

def count_numbers(n):
	first = 2
	second = 4
	if n == 1:
		return first
	elif n == 2:
		return second
	else :
		for i in range(2, n):
			new = first + second
			first = second
			second = new
		return second 

if __name__ == '__main__':
	n = int(input())
	print(count_numbers(n))
