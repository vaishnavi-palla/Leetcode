class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1 and bits[0] == 0:
            return True
        res = []
        i = 0
        while i <= len(bits)-1:
            if bits[i] == 0:
                res.append(1)
                i += 1
            elif bits[i] == 1 and bits[i+1] == 0:
                res.append(2)
                i += 2
            elif bits[i] == 1 and bits[i+1] == 1:
                res.append(2)
                i += 2
            else:
                res.append(0)
                i += 1
        for i in res:
            if i == 0:
                return False
            break
        if res[-1] == 1:
            return True
        else:
            return False