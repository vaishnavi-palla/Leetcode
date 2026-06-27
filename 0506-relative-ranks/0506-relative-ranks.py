class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dum = sorted(score)
        dum = dum[::-1]
        ranks = {}
        res = []
        for i,num in enumerate(dum):
            ranks[num] = i+1
        for s in score:
            rank = ranks[s]
            if rank == 1:
                res.append("Gold Medal")
            elif rank == 2:
                res.append("Silver Medal")
            elif rank == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(rank))
        return res