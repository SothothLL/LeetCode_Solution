# 逐个删除查找过的元素
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        nums.sort()
        while True:
            if i in nums:
                del nums[0]
                i += 1
            else:
                return i
                break

# 项数之和减数组元素之和即为缺失元素
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2-sum(nums)
