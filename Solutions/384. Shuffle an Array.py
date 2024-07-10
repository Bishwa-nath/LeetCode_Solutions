class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        new_arr = self.arr
        n = len(new_arr)
        for i in range(n):
            a = random.randint(0, n - 1)
            new_arr[a], new_arr[i] = new_arr[i], new_arr[a]

        return new_arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()