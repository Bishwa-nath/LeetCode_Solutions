class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = dict()
        for v in nums:
            d[v] = 1 + d.get(v, 0)

        ans = []
        for k, v in d.items():
            if v == 1:
                ans.append(k)

        return ans
