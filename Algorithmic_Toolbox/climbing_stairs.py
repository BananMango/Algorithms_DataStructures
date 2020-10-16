def climbStairs(n):
    ''' O(n) time complexity '''
    prev, curr = 1, 1
    for i in range(2, n+1):
        next_ = curr + prev
        prev = curr
        curr = next_
    return curr
    
if __name__ == '__main__':
  n = 4
  print(climbStairs(n))
