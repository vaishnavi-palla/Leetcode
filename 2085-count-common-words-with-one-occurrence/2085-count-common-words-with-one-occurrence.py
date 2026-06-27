class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        c = 0
        for word in counter1:
            if counter1[word] != 1:
                continue
            if word not in counter2:
                continue
            if counter2[word] == 1:
                c += 1
        return c