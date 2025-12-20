class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = [''.join(col) for col in zip(*strs)]
        res = 0
        for s in strs:
            if s != ''.join(sorted(s)):
                res += 1
        return res