class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        counter = 0
        arr = list(s)
        for i in range(len(arr)):
            if arr[i] == '(':
                counter += 1
            elif arr[i] == ')':
                if counter == 0:
                    arr[i] = '*'
                else:
                    counter -= 1

        for i in range(len(arr) - 1, -1, -1):
            if counter > 0 and arr[i] == '(':
                arr[i] = '*'
                counter -= 1

        result = ''.join(c for c in arr if c != '*')

        return result
