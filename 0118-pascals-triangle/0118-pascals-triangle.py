class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            level = []

            for j in range(i+1):
                level.append(1)   
            res.append(level)
        
        if numRows > 2:
            for i in range(2, numRows):
                for j in range(1, i):
                    res[i][j] = res[i-1][j-1]+res[i-1][j]
                
        return res
