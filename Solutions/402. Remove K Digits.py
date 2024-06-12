class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while stack and k > 0 and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)

        stack = stack[:-k] if k > 0 else stack

        result = ''.join(stack).lstrip('0')
        return result if result else '0'
