class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        counts = Counter(arr1)
        for i in arr2:
            for j in range(counts[i]):
                res.append(i)
        dum = set(arr1) - set(arr2)
        dum = list(dum)
        dum.sort()
        dum1 = []
        for i in dum:
            for j in range(counts[i]):
                dum1.append(i)
        return res+dum1