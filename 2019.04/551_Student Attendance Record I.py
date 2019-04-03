# Python语言特性天下第一
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False
        if "LLL" in s:
            return False
        return True
