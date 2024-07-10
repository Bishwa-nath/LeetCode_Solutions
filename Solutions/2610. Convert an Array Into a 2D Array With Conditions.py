class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = dict(Counter(nums))
        mx = max(counter.values())
        n = len(counter)
        ans = []
        for i in range(mx):
            temp = []
            for j in counter.keys():
                if counter[j] > 0:
                    temp.append(j)
                    counter[j] -= 1
            ans.append(temp)

        return ans

