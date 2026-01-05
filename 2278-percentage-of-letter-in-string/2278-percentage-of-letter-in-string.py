class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        req = 0
        for i in s:
            if i == letter:
                req += 1
        return int((req/len(s))*100)