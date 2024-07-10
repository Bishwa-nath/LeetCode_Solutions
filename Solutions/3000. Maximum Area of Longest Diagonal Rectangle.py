class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        dig = 0
        x, y = 0, 0
        for d in dimensions:
            digonal = math.sqrt(d[0] ** 2 + d[1] ** 2)
            if digonal > dig:
                ans = d[0] * d[1]
                dig = digonal
                x = d[0]
                y = d[1]
            elif digonal == dig:
                ans = max(ans, d[0] * d[1])

        return ans
