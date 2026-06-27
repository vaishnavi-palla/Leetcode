class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        req = sorted(counts.items(),key=lambda x : x[1],reverse = True)
        return [x[0] for x in req[:k]]