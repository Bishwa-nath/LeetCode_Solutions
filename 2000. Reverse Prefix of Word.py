class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        find_ch = word.find(ch)
        if find_ch > -1:
            temp = word[:find_ch+1]
            return temp[::-1] + word[find_ch+1:]

        return word