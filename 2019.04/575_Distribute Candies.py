class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        if len(candies)//2 > len(set(candies)):
            return len(set(candies))
        return len(candies)//2
