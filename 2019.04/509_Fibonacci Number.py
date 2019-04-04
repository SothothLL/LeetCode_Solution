# 递归
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return Solution.fib(self, N-1) + Solution.fib(self, N-2)

# 暴力求解
class Solution:
    def fib(self, N: int) -> int:
        a, b, c = 0, 1, 1

        if N == 0:
            return 0
        for i in range(N):
            a = b
            b = c
            c = a+b
        return a

# 通项公式
class Solution:
    def fib(self, N: int) -> int:
        return int((((1+5**0.5)/2)**N - ((1-5**0.5)/2)**N)/(5**0.5))
