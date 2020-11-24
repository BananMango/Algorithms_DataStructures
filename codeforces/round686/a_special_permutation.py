def main():
	n = int(input())
	for i in range(n):
		a = int(input())
		print(*[i for i in range(2, a + 1)] + [1])

if __name__ == '__main__':
	main()