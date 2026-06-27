class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        res = sorted(nums, key = lambda x: (int((bin(x)[2:])[::-1],2),x))
        return res