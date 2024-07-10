class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left = 0
        right = 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        for c in range(len(s) // 2):
            if s[c].lower() in vowel:
                left += 1
        for c in range(len(s) // 2, len(s)):
            if s[c].lower() in vowel:
                right += 1

        return left == right
