class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = 0
        curr = 0
        for v in nums:
            temp = pre
            pre = curr
            curr = max(v + temp, pre)

        return curr
