class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = list(set(nums1) ^ set(nums2))
        res1 = []
        res2 = []
        for i in res:
            if i in nums1:
                res1.append(i)
            else:
                res2.append(i)
        ares = []
        ares.append(res1)
        ares.append(res2)
        return ares