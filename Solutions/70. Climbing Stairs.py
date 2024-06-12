class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(1, n + 1):
            temp = a + b
            a = b
            b = temp
        return b
