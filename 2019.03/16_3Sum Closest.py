class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = None
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                j = i+1
                k = len(nums) - 1
                while j < k:
                    closest_num = nums[i] + nums[j] + nums[k]
                    difference = closest_num - target
                    if res is None or abs(res - target) > abs(difference):
                        res = closest_num
                    if difference == 0:
                        return target
                    elif difference < 0:
                        j += 1
                    else:
                        k -= 1
        return res
