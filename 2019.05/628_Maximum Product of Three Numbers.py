class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product_1 = nums[-1] * nums[-2] * nums[-3]
        product_2 = nums[-1] * nums[0] * nums[1]
        return max(product_1, product_2)
