class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even = 0
        for i in nums:
            if i%2==0:
                even+=1
                if even >= 2:
                    return True
        return False