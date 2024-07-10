class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        ans = 0
        for i in range(1, (n // 3) * 2 + 1, 2):
            ans += piles[i]

        return ans
