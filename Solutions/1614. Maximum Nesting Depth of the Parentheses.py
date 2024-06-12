class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        mx = 0
        for c in s:
            if c == '(':
                cnt += 1
                if mx < cnt:
                    mx = cnt
            if c == ')':
                cnt -= 1

        return mx
