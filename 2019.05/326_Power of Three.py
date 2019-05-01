class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        res = 1
        while res < n:
            res *= 3
        return res == n
