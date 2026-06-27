class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        stack = []
        maxi = 0
        for i in s:
            if i in stack:
                while stack[0] != i:
                    stack.pop(0)
                stack.pop(0)
            stack.append(i)
            maxi = max(len(stack),maxi)
        return maxi