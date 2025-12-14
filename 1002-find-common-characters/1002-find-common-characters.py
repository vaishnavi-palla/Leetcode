class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for ch in words[0]:
            for i in range(1,len(words)):
                if ch not in words[i]:
                    break
            else:
                res.append(ch)
                for i in range(len(words)):
                    words[i] = words[i].replace(ch,'',1)
        return res