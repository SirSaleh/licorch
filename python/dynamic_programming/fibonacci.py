"""
get the n'th memeber in sequence of Fibonacci number

    * base cases:
        F(0) = 0, F(1) = 1
    * Transition Functions
        F(n) = F(n-1) + f(n-2) for each n > 1
    * direction:
        up-bottom
    * result:
        memo[n]
"""
class Solution(object):

    def __init__(self):
        self.memo = {0: 0, 1: 1}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]


if __name__=="__main__":
    solver = Solution()

    assert solver.fib(0) == 0
    assert solver.fib(1) == 1
    assert solver.fib(2) == 1
    assert solver.fib(3) == 2
    assert solver.fib(4) == 3
    assert solver.fib(5) == 5
    assert solver.fib(6) == 8
    
        