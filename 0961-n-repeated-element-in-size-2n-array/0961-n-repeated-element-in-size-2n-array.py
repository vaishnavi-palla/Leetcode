class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counts = Counter(nums)
        n = len(nums)//2
        for i in counts:
            if counts[i] == n:
                return i