class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        if s.count('1') == len(s) or s.count('0') == len(s):
            return len(s) - 1

        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            zeros = left.count('0')
            ones = right.count('1')
            res = max(res, zeros + ones)

        return res
