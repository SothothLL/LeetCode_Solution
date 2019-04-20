class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0 or num & (num-1):
            return False
        return num & 0x55555555 == num
