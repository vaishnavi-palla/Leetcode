class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        for i in range (len(s)-1):
            if s[i] == s[i+1]:
                res += 1
        return (res+1)//2