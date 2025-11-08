class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        if res:
            return [min(res),max(res)]
        else:
            return [-1,-1]