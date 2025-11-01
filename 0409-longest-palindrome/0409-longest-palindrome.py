class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res,flag = 0,0
        for ch,cou in count.items():
            if cou%2==0:
                res+=cou
            else:
                res += cou-1
                flag = 1
        if flag %2== 1:
            return res+1
        else:
            return res