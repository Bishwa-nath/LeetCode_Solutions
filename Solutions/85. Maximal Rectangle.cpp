class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.empty() || matrix[0].empty())
            return 0;

        int rows = matrix.size();
        int cols = matrix[0].size();
        vector<int> heights(cols+1, 0);
        int res = 0;

        for(const auto& row: matrix) {
            for(int i=0; i<cols; i++) {
                heights[i] = (row[i] == '1') ? heights[i] + 1 : 0;
            }

            int n = heights.size();

            for(int i=0; i<n; i++) {
                for(int j=i, mnHt = INT_MAX; j<n; j++) {
                    mnHt = min(mnHt, heights[j]);
                    int area = mnHt * (j-i + 1);
                    res = max(res, area);
                }
            }
        }
        return res;
    }
};