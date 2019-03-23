# 直接递归提示超时,设置缓存
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2 or n == 1:
            return n
        else:
            temp = [1, 2]
            for i in range(2, n):
                temp.append(temp[i-1] + temp[i-2])
            return temp[-1]
