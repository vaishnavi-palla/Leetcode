class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = 0
        for i in range(1,int(num**0.5)+1):
            if num%i == 0:
                if i != num:
                    divisors += i
                if i != 1 and num // i != num :
                    divisors += num//i 
        return divisors == num