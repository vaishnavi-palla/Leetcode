class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x>0:
            while x > 0:
                rem = x%10
                rev = (rev*10 )+ rem
                x//=10
            if rev > 2**31 - 1:
                return 0
            else:
                return rev
        else:
            x = str(x)
            x = x[1:]
            if x != '':
                x = int(x)
            else:
                x = 0
            while x > 0:
                rem = x%10
                rev = (rev*10 )+ rem
                x//=10
            if -rev < -2**31:
                return 0
            else:
                return -rev
