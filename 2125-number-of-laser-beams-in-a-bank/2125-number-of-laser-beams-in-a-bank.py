class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        dum = []
        for row in bank:
            ones = 0
            for i in row:
                if i == '1':
                    ones += 1
            if ones != 0:
                dum.append(ones)
        res = []
        for i in range(len(dum)-1):
            res.append(dum[i]*dum[i+1])
        return sum(res)