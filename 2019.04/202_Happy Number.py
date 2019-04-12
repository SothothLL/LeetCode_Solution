class Solution:
    def isHappy(self, n: int) -> bool:
        tag, res = 0, 0
        if n == 1:
            return True
        if 1 < n < 5:
            return False
        while n:
            tag = n % 10
            res += tag**2
            n //= 10
        return Solution.isHappy(self, res)
