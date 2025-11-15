class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        first=letters[0]
        letters.sort()
        for i in letters:
            if ord(i)>ord(target):
                return i 
                break
        else:
            return first