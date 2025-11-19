class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = max(nums)
        res = [i for i in range(len(nums)) if maxi == nums[i]]
        for i in range(len(nums)):
            if nums[i]*2 > maxi and nums[i] != maxi:
                return -1
        else:
            return res[0]