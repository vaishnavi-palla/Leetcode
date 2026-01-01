class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        req = len(nums)/3
        counts = Counter(nums)
        res = []
        for i in counts:
            if counts[i] > req:
                res.append(i) 
        return res