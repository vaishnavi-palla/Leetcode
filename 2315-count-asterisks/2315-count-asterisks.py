class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split('|')
        res = 0
        for i in range(len(s)):
            if i%2 == 0:
                for j in s[i]:
                    if j == '*':
                        res += 1
        return res