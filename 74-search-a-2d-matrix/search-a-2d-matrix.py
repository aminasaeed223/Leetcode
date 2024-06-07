class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # a = len(matrix)
        # b = len(matrix[0])
        # for i in range(a):
        #     for j in range(b):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        a = len(matrix[0])
        b = len(matrix)
        r = 0
        for i in range(b):
            if matrix[i][0] <= target and matrix[i][a-1]>= target:
                r = i
                break
        for i in range(a):
            if target == matrix[r][i]:
                return True
        return False

        