class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = sorted(nums)
        n = len(nums)
        return res[n//2]
