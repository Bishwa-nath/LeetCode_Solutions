class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for d in digits:
            s += str(d)
        s = str(int(s) + 1)
        ans = []
        for d in s:
            ans.append(int(d))
        return ans
