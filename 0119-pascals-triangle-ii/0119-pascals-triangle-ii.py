class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):
            dum = [1]*(i+1)
            for j in range(1,i):
                dum[j] = res[i-1][j-1] + res[i-1][j]
            res.append(dum)
        return res[rowIndex]