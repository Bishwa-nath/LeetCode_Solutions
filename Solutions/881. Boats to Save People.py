class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        boat = 0
        n = len(people) - 1
        while i <= n:
            if people[i] + people[n] <= limit:
                i += 1

            boat += 1
            n -= 1

        return boat
