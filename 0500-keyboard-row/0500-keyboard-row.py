class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = ("qwertyuiopQWERTYUIOP")
        second = ("asdfghjklASDFGHJKL")
        third = ("zxcvbnmZXCVBNM")
        res = []
        for i in words:
            check = set()
            for j in i:
                if j in first:
                    check.add('1')
                elif j in second:
                    check.add('2')
                else:
                    check.add('3')
            if len(check) == 1:
                res.append(i)
        return res