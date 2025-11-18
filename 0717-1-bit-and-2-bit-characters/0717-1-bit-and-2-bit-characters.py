class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        res = []
        i = 0
        while i <= len(bits)-1:
            if bits[i] == 0:
                res.append(1)
                i += 1
            elif bits[i] == 1:
                res.append(2)
                i += 2
        if res[-1] == 1:
            return True
        else:
            return False