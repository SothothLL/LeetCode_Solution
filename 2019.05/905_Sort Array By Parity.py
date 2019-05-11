class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if A is None or len(A) == 1:
            return A
        left, right = 0, len(A)-1
        while left < right:
            if A[left] & 1 == 1 and A[right] & 1 == 0:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp
            elif A[left] & 1 == 0:
                left += 1
            elif A[right] & 1 == 1:
                right -= 1
        return A

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        a = []
        b = []
        for i in A:
            if i & 1 == 0:
                a.append(i)
            elif i & 1 == 1:
                b.append(i)
        return a+b
