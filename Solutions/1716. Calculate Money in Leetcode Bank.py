class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        q = n // 7
        rem = n % 7
        res = (q * (q - 1) // 2) * 7
        res += q * 28
        res += (rem * (rem + 1) // 2) + (q * rem)
        return res
