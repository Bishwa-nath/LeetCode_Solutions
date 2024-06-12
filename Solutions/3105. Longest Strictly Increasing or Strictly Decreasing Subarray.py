class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_len, dec_len, mx_len = 1, 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_len += 1
                dec_len = 1
            elif nums[i] < nums[i-1]:
                dec_len += 1
                inc_len = 1
            else:
                dec_len = 1
                inc_len = 1
            mx_len = max(mx_len, inc_len, dec_len)

        return mx_len
