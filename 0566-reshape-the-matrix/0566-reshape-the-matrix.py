class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        dum = []
        for row in mat:
            for j in row:
                dum.append(j)
        res1 = []
        index = 0
        if r*c != len(dum):
            return mat
        else:
            for i in range(r):
                res = []
                for j in range(c):
                    res.append(dum[index])
                    index += 1
                res1.append(res)

            return res1