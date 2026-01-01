class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams,prev = 0,0
        for row in bank:
            dev = row.count('1')
            if dev:
                beams += dev*prev
                prev = dev
        return beams