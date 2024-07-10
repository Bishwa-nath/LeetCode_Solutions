class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = [0] * 100001
        for w, l in matches:
            if losses[w] == 0:
                losses[w] = -1
            if losses[l] == -1:
                losses[l] = 1
            else:
                losses[l] += 1

        zero_lose = [i for i in range(1, 100001) if losses[i] == -1]
        one_lose = [i for i in range(1, 100001) if losses[i] == 1]
        return [zero_lose, one_lose]
