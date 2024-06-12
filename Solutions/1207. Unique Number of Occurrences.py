class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for a in arr:
            d[a] = 1 + d.get(a, 0)
        ls = d.values()
        return len(ls) == len(set(ls))
