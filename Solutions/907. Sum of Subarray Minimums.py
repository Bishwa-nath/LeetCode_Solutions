class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        stack = [0]
        ans = [0] * len(arr)

        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            ans[i] = ans[j] + (i - j) * arr[i]
            stack.append(i)

        return sum(ans) % (10 ** 9 + 7)
