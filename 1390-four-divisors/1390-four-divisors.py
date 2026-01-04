class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            check = 0
            divisors = 0
            for i in range(1,int(n**0.5)+1):
                if n%i == 0:
                    if i == n//i:
                        check+=1
                        divisors += i
                    else:
                        check += 2
                        divisors += i + (n//i)
            if check == 4:
                res += divisors
        return res