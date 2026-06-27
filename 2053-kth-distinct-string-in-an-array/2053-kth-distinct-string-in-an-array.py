class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        dum = []
        for w in arr:
            if count[w] == 1:
                dum.append(w)
        return dum[k-1] if k <= len(dum) else ""