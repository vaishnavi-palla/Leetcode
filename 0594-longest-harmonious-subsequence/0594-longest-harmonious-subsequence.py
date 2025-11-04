class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cou = Counter(nums)
        sort = sorted(cou.keys())
        res = 0
        for i in range(1,len(sort)):
            if sort[i] - sort[i-1] == 1:
                res = max(res,cou[sort[i]]+cou[sort[i-1]])
        return res