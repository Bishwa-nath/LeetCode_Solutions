class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mx = max(cnt.values())
        ans = 0
        for v in cnt.values():
            if v == mx:
                ans += 1

        return ans * mx
