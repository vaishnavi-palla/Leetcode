class Solution:
    def minimumChairs(self, s: str) -> int:
        res,maxi = 0,0
        for i in s:
            if i == 'E':
                res += 1
                maxi = max(res,maxi)
            if i == 'L':
                res -= 1 
        return maxi