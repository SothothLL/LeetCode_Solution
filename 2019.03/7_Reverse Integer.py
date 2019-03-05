class Solution:
    def reverse(self, x: 'int') -> 'int':
        n = x if x > 0 else -x
        res = 0
        while n:
            res = res * 10 + n % 10
            n = n // 10
        if res > 0x7fffffff:
            return 0
        return res if x > 0 else -res
