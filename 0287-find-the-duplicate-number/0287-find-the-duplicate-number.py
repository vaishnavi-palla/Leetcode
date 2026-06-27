class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        dups = [num for num,cou in counts.items() if cou > 1]
        return dups[0]