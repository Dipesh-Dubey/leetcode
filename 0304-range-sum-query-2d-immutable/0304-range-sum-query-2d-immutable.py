class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        r,c = len(matrix), len(matrix[0])
        self.ps = [[0 for _ in range(c)] for _ in range(r)]

        self.ps[0][0] = matrix[0][0]
        
        for i in range(c-1):
            self.ps[0][i+1] =  self.ps[0][i] + matrix[0][i+1] 

        for i in range(r-1):
            self.ps[i+1][0] =  self.ps[i][0] + matrix[i+1][0]
        
        for i in range(1,r):
            for j in range(1,c):
                self.ps[i][j] = self.ps[i][j-1] + self.ps[i-1][j] + matrix[i][j] - self.ps[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1>0 and col1 >0:
            return self.ps[row2][col2] - self.ps[row2][col1-1] - self.ps[row1-1][col2] + self.ps[row1-1][col1-1]
        else :
            if row1==0 and col1==0:
                return self.ps[row2][col2] 
            elif row1 <= 0 :
                return self.ps[row2][col2] - self.ps[row2][col1-1]
            elif col1 <=0 :
                return self.ps[row2][col2] - self.ps[row1-1][col2]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)