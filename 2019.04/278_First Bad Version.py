# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1) is True:
            return 1
        left, right = 1, n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid) is False:
                left = mid
            else:
                right = mid
            if left+1 == right or left == right:
                return right
