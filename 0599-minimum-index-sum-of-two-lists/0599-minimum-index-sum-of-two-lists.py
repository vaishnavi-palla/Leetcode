class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list_dic1 = {word:i for i,word in enumerate(list1)}
        list_dic2 = {word:i for i,word in enumerate(list2)}
        common = set(list_dic1) & set(list_dic2)
        indexs = {word : (list_dic1[word],list_dic2[word]) for word in common}
        mini =float('inf')
        for word,(i1,i2) in indexs.items():
            mini = min(mini,(i1+i2))
        res = []
        for word,(i1,i2) in indexs.items():
            if i1+i2 == mini:
                res.append(word)
        return res