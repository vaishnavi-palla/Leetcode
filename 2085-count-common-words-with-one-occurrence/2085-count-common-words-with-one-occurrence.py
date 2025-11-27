class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        count1 = [w for w,f in count1.items() if f == 1]
        count2 = [w for w,f in count2.items() if f == 1]
        res = []
        for i in count1:
            if i in count2:
                res.append(i)
        return len(res)