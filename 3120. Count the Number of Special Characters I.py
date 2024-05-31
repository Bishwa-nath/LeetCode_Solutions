class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upperSet = set()
        lowerSet = set()
        for c in word:
            if c.isupper():
                upperSet.add(c)
            if c.islower():
                lowerSet.add(c)

        res = 0
        for c in upperSet:
            if c.lower() in lowerSet:
                res += 1

        return res
