class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        jobs_num = len(profit)

        dp = [0] * (jobs_num + 1)
        for i, (et, st, pro) in enumerate(jobs):
            idx = bisect_right(jobs, st, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[idx] + pro)

        return dp[jobs_num]
