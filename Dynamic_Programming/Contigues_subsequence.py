def calculate_max(array):
	n = len(array)
	L = [0] * n
	for i in range(1, n):
		for j in range(1, i-1):
			L[i] = array[i] + max(0, L[i-1])
	return max(L)

if __name__ == '__main__':
	array = [5, 15, -30, 10, -5, 40, 10]
	max_ = calculate_max(array)
	print(max_)
