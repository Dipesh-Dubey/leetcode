class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n = len(grid),len(grid[0])
        sum = 0
        for i in range(m):
            for j in range(n):
                sum += grid[i][j]

        if sum%2 != 0:
            return False
        else:
            sum = sum//2
            r_s , c_s = [0]*m, [0]*n

            for i in range(m):
                for j in range(n):
                    r_s[i] += grid[i][j]

            for j in range(n):
                for i in range(m):
                    c_s[j] += grid[i][j]
            
            w_s = 0
            for num in r_s:
                w_s += num
                if w_s == sum: return True
                elif w_s > sum: break
            
            w_s = 0
            for num in c_s:
                w_s += num
                if w_s == sum: return True
                elif w_s > sum: break
            
            return False

            



        

