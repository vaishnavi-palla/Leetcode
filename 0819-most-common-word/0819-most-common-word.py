class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = []
        for word in paragraph.replace('.',' ').replace(',',' ').split():
            dum = ''
            for i in word:
                if i.isalpha():
                    dum = dum+i
            para.append(dum.lower())
        dum = []
        for word in para:
            if word not in banned:
                dum.append(word)
        counts = Counter(dum)
        maxi = max(counts,key=counts.get)
        return maxi