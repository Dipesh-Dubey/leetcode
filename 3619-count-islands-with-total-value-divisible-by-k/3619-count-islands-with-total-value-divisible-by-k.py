class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return 0

        rows,cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            val = grid[r][c]
            grid[r][c] = 0

            return (val + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        counter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    total = dfs(r, c)
                    if total % k == 0:
                        counter += 1

        return counter