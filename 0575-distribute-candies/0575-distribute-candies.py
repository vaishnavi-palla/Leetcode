class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        vari = set(candyType)
        can_eat = len(candyType)//2
        if len(vari) < can_eat:
            return len(vari)
        else:
            return can_eat