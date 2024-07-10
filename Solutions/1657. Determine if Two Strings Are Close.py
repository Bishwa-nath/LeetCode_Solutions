class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = {}
        w2 = {}
        if len(word1) != len(word2):
            return False
        for c in word1:
            w1[c] = 1 + w1.get(c, 0)
        for c in word2:
            w2[c] = 1 + w2.get(c, 0)

        sorted_w1 = sorted(w1.values())
        sorted_w2 = sorted(w2.values())

        key_match = set(w1.keys()) == set(w2.keys())

        return sorted_w1 == sorted_w2 and key_match
