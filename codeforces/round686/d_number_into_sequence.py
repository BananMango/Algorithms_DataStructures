import math
from collections import Counter


def prime_factorization(n):
    prime_factors = list()

    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n / i
    if n > 2:
        prime_factors.append(n)

    return prime_factors


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        prime_factors = prime_factorization(n)
        prime_factors = Counter(prime_factors)

        p = -1
        most = 0
        for prime in prime_factors:
            if prime_factors[prime] > most:
                most = prime_factors[prime]
                p = prime

        print(most)

        arr = [p] * most
        while n % p == 0:
            n = n // p
        arr[-1] *= n
        print(*arr)


if __name__ == '__main__':
    main()
