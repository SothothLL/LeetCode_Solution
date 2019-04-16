class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = set("qwertyuiopQWERTYUIOP")
        row_2 = set("asdfghjklASDFGHJKL")
        row_3 = set("zxcvbnmZXCVBNM")
        res = []

        for word in words:
            if set(word) <= row_1 or set(word) <= row_2 or set(word) <= row_3:
                res.append(word)
        return res
