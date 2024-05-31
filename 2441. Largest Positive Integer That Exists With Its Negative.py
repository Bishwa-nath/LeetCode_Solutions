class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for n in nums:
            if n < 0 and n * (-1) in nums:
                return n * (-1)

        return -1

