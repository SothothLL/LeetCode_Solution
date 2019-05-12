class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        left = 0
        right = len(A)-1
        if right < 2:
            return False
        elif A[0] < A[1] and A[right-1] > A[right]:
            while A[left] < A[left+1]:
                left += 1
            while A[right-1] > A[right]:
                right -= 1
            return left == right
        else:
            return False
