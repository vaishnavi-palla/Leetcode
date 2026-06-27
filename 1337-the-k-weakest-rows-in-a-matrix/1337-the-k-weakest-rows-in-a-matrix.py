class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dum = {}
        for i in range(len(mat)):
            dum[i] = sum(mat[i])
        res = sorted(dum,key = dum.get)
        return res[:k]