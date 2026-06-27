class Solution:
    def frequencySort(self, s: str) -> str:
        res=""
        freq=Counter(s)
        l=[]
        for element,count in freq.items():
            l.append([count,element])
        l.sort(reverse=True)
        for i in l:
            res+=(i[1]*i[0])
        return res