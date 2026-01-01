class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = [i for i in nums if i%2==0]
        if not nums:
            return -1
        counts = Counter(nums)
        max_freq = max(counts.values())
        res = [num for num,freq in counts.items() if freq == max_freq]
        if res:
            return min(res)
        else:
            return -1