class Solution:
    def countValidWords(self, sentence: str) -> int:
        res = 0
        for word in sentence.split():
            hyphen = 0
            punct = 0
            valid = True

            for i,ch in enumerate(word):
                if ch.isdigit():
                    valid = False
                    break
                if ch in '!.,':
                    if i != len(word)-1:
                        valid = False
                        break
                    punct += 1
                    if punct > 1:
                        valid = False
                        break
                elif ch == '-':
                    if i == 0 or i == len(word)-1 or not word[i-1].isalpha() or not word[i+1].isalpha():
                        valid = False
                        break
                    hyphen += 1
                    if hyphen > 1:
                        valid = False
                        break
                elif not ch.isalpha():
                    valid = False
                    break
            if valid:
                res += 1
        return res