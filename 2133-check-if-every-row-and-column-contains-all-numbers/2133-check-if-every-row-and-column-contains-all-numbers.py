class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        lst = [i+1 for i in range (n)]
        counts = Counter(i for row in matrix for i in row)
        for num,freq in counts.items():
            if freq>n:
                return False

        for row in matrix:
            if len(set(row)) != len(lst):
                return False
            for i in row:
                if i not in lst:
                    return False

        for i in range(n):
            seen = set()
            for j in range(n):
                if matrix[j][i] not in lst:
                    return False
                seen.add(matrix[j][i])
            if len(seen) != len(lst):
                return False
        return True