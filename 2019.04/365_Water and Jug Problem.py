class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0 or x + y == z:
            return True
        elif x+y < z:
            return False
        irp = Solution.relativelyPrime(self, x, y)
        if irp == 0:
            return z == 0
        return z % irp == 0

    def relativelyPrime(self, x: int, y: int) -> int:
        if y == 0:
            return x
        return Solution.relativelyPrime(self, y, x % y)
