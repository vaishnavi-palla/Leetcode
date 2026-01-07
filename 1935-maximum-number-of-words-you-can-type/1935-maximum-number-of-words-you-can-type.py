class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        n = 0
        for word in text:
            valid = True
            for i in word:
                if i in brokenLetters:
                    valid = False
            if valid:
                n += 1
        return n