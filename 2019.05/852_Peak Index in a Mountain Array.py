class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        right = len(A)-1
        while A[left] < A[left+1]:
            left += 1
        while A[right-1] > A[right]:
            right -= 1
        return A[left].index()
