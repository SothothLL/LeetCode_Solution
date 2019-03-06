class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if strs == []:
            return ""
        elif n == 1:
            return strs[0]
        elif n > 1:
            prefix = ""
            for index, i in enumerate(strs[0]):
                prefix += i
                for j in range(1, n):
                    if prefix not in strs[j][:index+1]:
                        break
                else:
                    continue
                break
            else:
                return prefix
            return prefix[:-1]
