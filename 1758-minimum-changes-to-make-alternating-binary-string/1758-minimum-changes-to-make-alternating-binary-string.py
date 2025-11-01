class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        count2 = 0
        
        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch != '0':
                    count1 += 1
                if ch != '1':
                    count2 += 1
            else:
                if ch != '1':
                    count1 += 1
                if ch != '0':
                    count2 += 1
                    
        return min(count1, count2)