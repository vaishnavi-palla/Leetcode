class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        curr,maxi = 0,0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1] > nums[i+2]:
                curr = nums[i]+nums[i+1]+nums[i+2]
                maxi = max(curr,maxi)
        return maxi