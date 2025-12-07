class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = int(num[::-1])
        return str(num)[::-1]