class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = {}
        t_freq = {}

        for c in s:
            s_freq[c] = s_freq.get(c, 0) + 1

        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        ans = 0
        for c in set(s) | set(t):
            ans += abs(s_freq.get(c, 0) - t_freq.get(c, 0))

        return ans // 2
