class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            if self.isSelfDividingNumber(i):
                res.append(i)
        return res

    def isSelfDividingNumber(self, num: int) -> bool:
        temp = num
        while temp != 0:
            if temp % 10 == 0 or num % (temp % 10) != 0:
                return False
            temp //= 10
        return True
