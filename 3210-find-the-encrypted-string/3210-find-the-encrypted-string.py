class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k = k%len(s)
        last = s[:k]
        first = s[k:]
        return first+last