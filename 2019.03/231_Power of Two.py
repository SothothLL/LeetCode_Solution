# 2的幂问题可以转换为比较二进制数的位运算问题


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return n & (n-1) == 0
