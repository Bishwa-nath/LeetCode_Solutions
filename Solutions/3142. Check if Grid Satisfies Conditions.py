class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if i < n- 1 and grid[i][j] != grid[i+1][j]:
                    return False
                if j < m - 1 and grid[i][j] == grid[i][j+1]:
                    return False

        return True
