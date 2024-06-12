class Solution:
    def maxLength(self, arr: List[str]) -> int:
        mxlen = [0]
        self.back_track(arr, '', 0, mxlen)
        return mxlen[0]

    def back_track(self, arr, curr, start, mxlen):
        if mxlen[0] < len(curr):
            mxlen[0] = len(curr)

        for i in range(start, len(arr)):
            if not self.isValid(curr, arr[i]):
                continue
            self.back_track(arr, curr + arr[i], i + 1, mxlen)

    def isValid(self, curr_str, new_str):
        ch_st = set()
        for ch in new_str:
            if ch in ch_st:
                return False

            ch_st.add(ch)
            if ch in curr_str:
                return False

        return True
