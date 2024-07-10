class Solution:
    def largestOddNumber(self, num: str) -> str:

        idx = -1
        for i in range(len(num)-1, -1, -1):
            if int(num[i])%2:
                idx = i
                break

        return num[:idx+1]