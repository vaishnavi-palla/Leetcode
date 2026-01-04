class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            check = 0
            divisors = 0
            for j in range(1,i+1):
                if i%j == 0:
                    check+=1
                    divisors += j
            if check == 4:
                res += divisors
        return res