class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        n = 0
        for word in text.split():
            for i in word:
                if i in brokenLetters:
                    break
            else:
                n += 1
        return n