# 直接递归提示超时,设置缓存
# 归纳发现是斐波那契数列 F(n)=F(n-1)+F(n-2)
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a+b
        return a
