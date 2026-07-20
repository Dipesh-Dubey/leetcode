class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows,cols = len(grid),len(grid[0])
        new = [[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                i,j = r, (c + k)% cols
                if c+k >= cols: 
                    i += (c+k)//cols
                    if i>=rows: i = i%rows
                new[i][j] = grid[r][c] 
                # print(new)
        
        return new