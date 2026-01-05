class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        res = [s[0],s[1]]
        for i in range(2,len(s)):
            if not (res[-1] == s[i] and res[-2] == s[i]):
                res.append(s[i])
        return ''.join(res)