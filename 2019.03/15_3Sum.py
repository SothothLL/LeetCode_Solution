class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    l = nums[i] + nums[j] +nums[k]
                    if l == 0:
                        res.append([nums[i],nums[j],nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while k > j and nums[k] == nums[k+1]:
                            k -= 1
                    elif l > 0:
                        k -= 1
                    else:
                        j += 1
        return res
