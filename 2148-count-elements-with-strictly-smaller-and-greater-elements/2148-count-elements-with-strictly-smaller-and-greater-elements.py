class Solution:
    def countElements(self, nums: List[int]) -> int:
        small = min(nums)
        big = max(nums)
        res = []
        for i in nums:
            if i != small and i != big:
                res.append(i)
        return len(res)