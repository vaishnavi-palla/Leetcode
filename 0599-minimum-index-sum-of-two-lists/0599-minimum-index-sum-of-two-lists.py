class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_dic1 = {word:i for i,word in enumerate(list1)}
        mini =float('inf')
        
        res = []
        for j,word in enumerate(list2):
            if word in list1:
                total = j+index_dic1[word]
                if total<mini:
                    mini = total
                    res = [word]
                elif total == mini:
                    res.append(word)
        return res