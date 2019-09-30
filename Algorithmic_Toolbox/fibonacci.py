# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
	arr = list(range(n+1))
	for i in range(2, n+1):
		arr[i] = arr[i-1] + arr[i-2]
	return arr[n]

n = int(input())
print(calc_fib_fast(n))
