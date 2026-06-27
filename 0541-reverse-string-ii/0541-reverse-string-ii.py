class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        parts = [s[i:i+k] for i in range(0,len(s),k)]
        res = []
        for i in range (len(parts)):
            if i%2!=0:
                res.append(parts[i])
            else:
                res.append(parts[i][::-1])
        return ''.join(res)