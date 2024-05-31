class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        for i in range(1, n - 1):
            temp = []
            for j in range(1, n - 1):
                mx = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        mx = max(mx, grid[k][l])
                temp.append(mx)
            res.append(temp)

        return res
