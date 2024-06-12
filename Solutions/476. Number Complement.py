class Solution:
    def findComplement(self, num: int) -> int:
        bits = 0
        temp = num
        while num:
            num //= 2
            bits += 1

        n = 2 ** bits - 1
        return (n - temp)
