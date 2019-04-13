class Solution:
    def firstUniqChar(self, s: str) -> int:
        tmp = list(set(s))
        tmp.sort(key=s.index)
        for i in tmp:
            if s.count(i) == 1:
                return s.index(i)
        return -1
