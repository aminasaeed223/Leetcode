class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_of_d = 0
        for i in range(len(mat)):
            sum_of_d = sum_of_d + mat[i][i]
        j = len(mat)-1
        for i in range (len(mat)):
            if i != j:
                sum_of_d = sum_of_d + mat[i][j]
            j = j-1
        return sum_of_d
        