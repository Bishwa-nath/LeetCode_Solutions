class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = permutations(nums)
        for p in perm:
            if list(p) not in ans:
                ans.append(list(p))

        return ans