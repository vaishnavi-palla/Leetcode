class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispal(sub):
            return sub == sub[::-1]
        l, r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]:
                return ispal(s[l+1:r+1]) or ispal(s[l:r])
            l += 1
            r -= 1
        return True