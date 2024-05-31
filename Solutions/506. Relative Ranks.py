class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank = {}
        for i, v in enumerate(sorted_score):
            if i < 3:
                rank[v] = medals[i]
            else:
                rank[v] = str(i + 1)

        return [rank[s] for s in score]