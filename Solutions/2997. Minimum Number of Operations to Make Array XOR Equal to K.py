class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        init_xor = 0
        for n in nums:
            init_xor = init_xor ^ n

        count = 0
        while k or init_xor:
            if (k % 2) != (init_xor % 2):
                count += 1
            k //= 2
            init_xor //= 2

        return count
