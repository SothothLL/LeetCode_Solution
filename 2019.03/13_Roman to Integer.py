class Solution:
    def romanToInt(self, s: str) -> int:
        roman_integer = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num, pre = 0, 1000
        for i in [roman_integer[j] for j in s]:
            num, pre = num + i - 2 * pre if i > pre else num + i, i
        return num
