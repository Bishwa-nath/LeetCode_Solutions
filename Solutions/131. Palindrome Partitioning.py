class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for e in range(start+1, len(s)+1):
                if is_palindrome(s[start:e]):
                    backtrack(e, path+[s[start:e]])

        res = []
        backtrack(0, [])
        return res