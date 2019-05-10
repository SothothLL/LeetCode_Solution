class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        count = 1
        temp = count
        while temp < num:
            count += 2
            temp += count
        return temp == num
