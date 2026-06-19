class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = len(matrix),len(matrix[0])
        flag_r,flag_d = False,False

        for j in range(c):
            if matrix[0][j]==0:
                flag_r = True
                break
        for i in range(r):
            if matrix[i][0]==0:
                flag_d = True
                break

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][0] = "r"
                    matrix[0][j] = "d"
        
        print(matrix)
        for i in range(1,r):
            if matrix[i][0] == "r":
                matrix[i] = [0]*c
        print(matrix)
        for j in range(c):
            if matrix[0][j] == "d":
                for i in range(r):
                    matrix[i][j] = 0
        
        if flag_r == True: 
            matrix[0] = [0]*c
        if flag_d == True: 
            for i in range(r):
                    matrix[i][0] = 0     
            
        
