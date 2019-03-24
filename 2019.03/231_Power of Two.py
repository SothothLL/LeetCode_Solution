# 2的幂问题可以转换为比较二进制数的位运算问题


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        return n & (n-1) == 0
