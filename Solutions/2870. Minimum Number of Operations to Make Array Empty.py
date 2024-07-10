class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = dict(Counter((nums)))
        if min(counter.values()) == 1:
            return -1

        ans = 0
        for v in counter.values():
            if v % 3 == 0:
                ans += (v // 3)
            else:
                ans += (v // 3) + 1

        return ans
