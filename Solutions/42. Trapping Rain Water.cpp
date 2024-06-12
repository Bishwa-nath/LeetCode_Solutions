class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        int maxl = height[l];
        int maxr = height[r];
        int res = 0;

        while(l < r) {
            if(maxl < maxr) {
                l += 1;
                maxl = max(maxl, height[l]);
                res += maxl - height[l];
            } else {
                r -= 1;
                maxr = max(maxr, height[r]);
                res += maxr - height[r];
            }
        }
        return res;

    }
};