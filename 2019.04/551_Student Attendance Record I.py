class Solution:
    def checkRecord(self, s: str) -> bool:
        count_absent = 0
        num = [-3, -2]
        for count, char in enumerate(s):
            if char is 'A':
                count_absent += 1
                if count_absent > 1:
                    return False
            elif char == 'L':
                num.append(count)
                if num[-3]+2 == num[-1]:
                    return False
        return True
