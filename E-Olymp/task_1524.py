def count_decomp(number, n):
	matrix = [[ 0 for i in range(72)] for j in range(72)]
	for i in range(72):
		matrix[1][i] = 1
		matrix[i][0] = 1
	for i in range(2, 72):
		for j in range(1, 72):
			matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
	return matrix[number+1][n -1]

if __name__ == '__main__':
	n = int(input())
	for i in range(n):
		n, t, p = map(int, input().split())
		number = t - n*p
		print(count_decomp(number, n))