class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res,curr = 0,0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                curr += 1
            else:
                res = max(res,curr+1)
                curr = 0
        res = max(res,curr+1)
        return res