class Solution:
    def fillCups(self, amount: List[int]) -> int:
            if amount[0] == 0 and amount[1] == 0 and amount[2] == 0:
                return 0
            elif amount[0] == 0 and amount[1] == 0 and amount[2] > 0:
                return amount[2]
            elif amount[0] == 0 and amount[1] > 0 and amount[2] == 0:
                return amount[1]
            elif amount[0] > 0 and amount[1] == 0 and amount[2] == 0:
                return amount[0]
            else:
                summ = sum(amount)
                return (summ%2) + (summ//2)