class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        dum = sorted(nums)
        if dum[-2]*2 <= dum[-1]:
            return nums.index(dum[-1])
        else:
            return -1