class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        island_area = {}
        island_id = 2

        def dfs(r, c, island_id):
            if (
                r < 0 or r >= n or
                c < 0 or c >= n or
                grid[r][c] != 1
            ):
                return 0

            grid[r][c] = island_id

            return (
                1
                + dfs(r + 1, c, island_id)
                + dfs(r - 1, c, island_id)
                + dfs(r, c + 1, island_id)
                + dfs(r, c - 1, island_id)
            )

        # Step 1: Label every island and store its area
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area = dfs(r, c, island_id)
                    island_area[island_id] = area
                    island_id += 1

        # If there were no zeros, whole grid is one island
        ans = max(island_area.values(), default=0)

        # Step 2: Try converting each 0 to 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    size = 1

                    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr, nc = r + dr, c + dc

                        if (
                            0 <= nr < n and
                            0 <= nc < n and
                            grid[nr][nc] > 1
                        ):
                            idx = grid[nr][nc]
                            if idx not in seen:
                                seen.add(idx)
                                size += island_area[idx]

                    ans = max(ans, size)

        return ans