class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        res = sorted(counts.keys(),key = lambda x: counts[x],reverse = True)
        return ''.join(ch*counts[ch] for ch in res)