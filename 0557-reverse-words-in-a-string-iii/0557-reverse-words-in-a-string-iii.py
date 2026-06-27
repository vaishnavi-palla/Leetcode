class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = [i[::-1]+' ' for i in s]
        return ''.join(res).strip()