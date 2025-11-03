class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        dum = []
        for row in mat:
            dum.extend(row)
        res = []
        for i in range(r):
            res.append(dum[:c])
            dum = dum[c:]
        return res