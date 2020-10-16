def climbStairs(n):
    ''' O(n) time complexity '''
    prev, curr = 1, 1
    for i in range(2, n+1):
        next_ = curr + prev
        prev = curr
        curr = next_
    return curr
    
def climbingStairs_fast(n):
    ''' Using Fibonacci formula '''
    import math
    a = (1 + math.sqrt(5)) / 2
    b = (1 - math.sqrt(5)) / 2
    res = math.pow(a, n+1) - math.pow(b, n+1)
    return int(res / math.sqrt(5))    

if __name__ == '__main__':
  n = 4
  print(climbStairs(n))
  print(climbingStairs_fast(n))
