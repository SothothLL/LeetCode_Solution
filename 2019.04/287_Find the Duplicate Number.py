# 排序后重复元素前后连续，判断前后元素是否相同。
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]

# 快慢指针，环入口即为重复元素。
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                fast = 0
                while nums[slow] != nums[fast]:
                    fast = nums[fast]
                    slow = nums[slow]
                return nums[slow]
