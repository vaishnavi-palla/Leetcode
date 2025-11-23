class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        res = []
        for i in str(n):
            if i != '0':
                res.append(int(i))
        summ = sum(res) 
        num = [str(i) for i in res]
        num = ''.join(num)
        num = int(num)
        return summ*num