def calculate_power(a, p):
    res = 1
    while p:
        if p & 0x1:
            res *= a
        a *= a
        p >>= 1
    return res
    
if __name__ == '__main__':
    n = 13
    power = 5
    res = calculate_power(n, power)
    print(res)
