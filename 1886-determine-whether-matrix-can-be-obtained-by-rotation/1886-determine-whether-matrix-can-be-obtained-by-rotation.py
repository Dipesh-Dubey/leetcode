class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        r,c = len(mat), len(mat[0])
        for _ in range(4):
            for i in range(r):
                for j in range(i,r):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

            for i in range(r):
                for j in range(c):
                    if j == c//2:
                        break
                    mat[i][j],mat[i][c-1-j] = mat[i][c-1-j],mat[i][j]
            
            if mat == target:
                return True
        
        return False