class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse = True)
        boxs = 0
        for cap in capacity:
            total_apples -= cap
            boxs += 1
            if total_apples<=0:
                return boxs
            
        return boxs