class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        r,c = len(grid), len(grid[0])

        top = x
        bottom = x+k-1

        while top<=bottom:
            for j in range(y,y+k):
                grid[top][j],grid[bottom][j] = grid[bottom][j],grid[top][j]
            print(grid)
            top+=1
            bottom-=1
        
        return grid