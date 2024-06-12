class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        num = sorted(nums[1:])
        return nums[0] + num[0] + num[1]
