class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        n = 0
        for word in text:
            for i in word:
                if i in brokenLetters:
                    break
            else:
                n += 1
        return n