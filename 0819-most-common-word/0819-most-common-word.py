class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para = re.split(r'[\!\?\'\,;:.\s]+', paragraph.lower())
        dum = [w for w in para if w and w not in banned]
        counts = Counter(dum)
        maxi = max(counts,key=counts.get)
        return maxi