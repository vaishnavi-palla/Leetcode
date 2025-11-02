class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        dum = []
        for i in nums:
            dum.append(i*i)
        return sorted(dum)