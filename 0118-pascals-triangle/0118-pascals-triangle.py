class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            dum = [1]*(i+1)
            for j in range(1,i):
                dum[j] = res[i-1][j-1] + res[i-1][j]
            res.append(dum)
        return res