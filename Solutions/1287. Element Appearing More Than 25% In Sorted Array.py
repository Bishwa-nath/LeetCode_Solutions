class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = {}
        for n in arr:
            d[n] = 1 + d.get(n, 0)

        for k, v in d.items():
            if v == max(d.values()):
                return k
