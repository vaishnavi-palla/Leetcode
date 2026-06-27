class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = []
        counts = Counter(nums)
        double = [num for num,cou in counts.items() if cou > 1]
        for i in range(1,len(nums)+1):
            if i not in nums:
                missing.append(i)
        return double+missing