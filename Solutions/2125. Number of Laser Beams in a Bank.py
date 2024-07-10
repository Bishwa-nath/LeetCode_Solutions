class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        n = len(bank)
        a = bank[0].count('1')
        for i in range(1, n):
            b = bank[i].count('1')
            ans += (a * b)
            if b:
                a = b

        return ans
