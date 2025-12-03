class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newnums = [0]*(len(nums)-1)
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1] < 10:
                    newnums[i] = nums[i]+nums[i+1]
                else:
                    newnums[i] = (nums[i]+nums[i+1])%10
            nums = newnums
        return nums[0]