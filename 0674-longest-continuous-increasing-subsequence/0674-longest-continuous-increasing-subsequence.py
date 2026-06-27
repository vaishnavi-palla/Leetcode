class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res,curr = 1,1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                curr += 1
                res = max(res,curr)
            else:
                curr = 1
        return res