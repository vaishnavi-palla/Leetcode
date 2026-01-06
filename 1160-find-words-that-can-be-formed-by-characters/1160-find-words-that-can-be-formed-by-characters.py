class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = []
        for word in words:
            flag = True
            for ch in word:
                if ch not in chars:
                    flag = False
            if flag == True: res.append(len(word))
        return sum(res)