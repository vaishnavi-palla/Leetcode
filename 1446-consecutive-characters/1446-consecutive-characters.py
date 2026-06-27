class Solution:
    def maxPower(self, s: str) -> int:
        res,curr = 1,1
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                curr += 1
            else:
                res = max(res,curr)
                curr = 1
        res = max(res,curr)
        return res