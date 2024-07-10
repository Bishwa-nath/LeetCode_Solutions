class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = [0] * 26
        res = 0

        for c in chars:
            counts[ord(c) - ord('a')] += 1

        for w in words:
            if self.can_word(w, counts):
                res += len(w)

        return res

    def can_word(self, word, counts):
        c = [0] * 26
        for w in word:
            x = ord(w) - ord('a')
            c[x] += 1
            if c[x] > counts[x]:
                return False

        return True
