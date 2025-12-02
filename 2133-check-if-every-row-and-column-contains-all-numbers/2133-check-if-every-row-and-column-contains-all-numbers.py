class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row in matrix:
            if len(set(row)) != n:
                return False
        for i in range(n):
            seen = set()
            for j in range(n):
                seen.add(matrix[j][i])
            if len(seen) != n:
                return False
        return True