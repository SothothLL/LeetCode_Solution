class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        res = []
        for i in nums:
            dic[i] = dic.get(i, 1)+1
        list_1 = list(dic.items())
        list_1.sort(key=lambda x: x[1], reverse=True)
        for elem, fre in list_1:
            res.append(elem)
            k -= 1
            if k == 0:
                break
        return res
