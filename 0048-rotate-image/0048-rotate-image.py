class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = len(matrix), len(matrix[0])
        for j in range(c):
            for i in range(j,r):
                if i == j:
                    pass
                else:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(r):
            for j in range(c):
                if j == c//2:
                    break
                matrix[i][j],matrix[i][c-1-j] = matrix[i][c-1-j],matrix[i][j]
   
        
        

