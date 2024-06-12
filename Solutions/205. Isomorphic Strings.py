class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        idxs = [0] * 150
        idxt = [0] * 150

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if idxs[ord(s[i])] != idxt[ord(t[i])]:
                return False
            idxs[ord(s[i])] = i + 1
            idxt[ord(t[i])] = i + 1

        return True
