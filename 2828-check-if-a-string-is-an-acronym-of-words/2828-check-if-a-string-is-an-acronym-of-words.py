class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        req = [word[0] for word in words]
        res = ''.join(req)
        return res == s