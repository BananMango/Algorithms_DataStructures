def calculate_power(a, p):
    res = 1
    while p:
        if p & 0x1:
            res *= a
        a *= a
        p >>= 1
    return res

def power_simple(a, n):
    res = 1
    while (n != 0):
        if (n % 2 == 1):
            res *= a
        a *= a
        n = n // 2
    return res

def power_simple2(a, n):
    negative_power = False
    if n < 0:
        n *= -1
        negative_power = True
	res = 1
    while(n != 0):
		if (n % 2 == 1):
			res *= x
		x *= x
        n = n // 2
	if negative_power:
		return 1 / res
	return res
    
if __name__ == '__main__':
    n = 13
    power = 5
    res = calculate_power(n, power)
    print(res)
    res = power_simple(n, power)
    print(res)
