class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opp = 0
        for i in nums:
            if i%3 != 0:
                if (i+1)%3 ==0 :
                    opp+=1
                if (i-1)%3 == 0:
                    opp+=1
        return opp