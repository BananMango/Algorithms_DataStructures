def min_value(t, a, b, c, n):
	t[1] = a[1]
	t[2] = min(a[1] + a[2], b[1])
	for i in range(3, n + 1):
		t[i] = min(
				t[i - 1] + a[i], 
				t[i - 2] + b[i - 1], 
				t[i - 3] + c[i - 2]
			)
	return t[n]

def read_values(n):
	a, b, c = [0] * (n+1), [0] * (n+1), [0] * (n+1)
	for i in range(1, n+1):
		a_i, b_i, c_i = map(int, input().split())
		a[i], b[i], c[i] = a_i, b_i, c_i
	return a, b, c

if __name__ == '__main__':
	n = int(input())
	t = [0] * (n + 1)
	a, b, c = read_values(n)
	print(min_value(t, a, b, c, n))
