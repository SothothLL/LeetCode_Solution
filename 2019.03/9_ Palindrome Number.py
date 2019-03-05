class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x if x > 0 else -x
        n_bef = n
        res = 0
        while n:
            res = res * 10 + n % 10
            n = n // 10

        if res > 0x7fffffff:
            return False
        else:
            n_now = res if x > 0 else -res

        return True if n_bef == n_now else False
