class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tem = sorted(set(arr))
        rank = {}
        for i,num in enumerate(tem,start = 1):
            rank[num] = i
        res = []
        for i in arr:
            res.append(rank[i])
        return res