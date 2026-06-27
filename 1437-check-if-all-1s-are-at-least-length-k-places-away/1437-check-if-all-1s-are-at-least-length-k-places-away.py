class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        pre = None
        for i,num in enumerate(nums):
            if num == 1:
                if pre is not None and i - pre <= k:
                    return False
                pre = i   
        return True