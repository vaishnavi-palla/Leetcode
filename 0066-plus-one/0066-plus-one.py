class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''.join(str(j) for j in digits)
        i=int(s)+1
        return[int(z) for z in str(i)]