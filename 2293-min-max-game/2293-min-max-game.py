class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums)>1:
            newnums = [0]*(len(nums)//2)
            for i in range(len(nums)//2):
                if i%2==0:
                    newnums[i]=min(nums[2*i],nums[2*i+1])
                else:
                    newnums[i]=max(nums[2*i],nums[2*i+1])
            nums = newnums
        return nums[0]