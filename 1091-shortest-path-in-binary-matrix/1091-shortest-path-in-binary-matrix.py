class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1: #edge case
            return -1

        q = deque([(0,0,1)])
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

        while q:
            for _ in range(len(q)):
                r, c, short = q.popleft()

                if r == rows - 1 and c == cols - 1:
                    return short

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0):
                        grid[nr][nc] = 1
                        q.append((nr, nc, short+1))
        
        return -1