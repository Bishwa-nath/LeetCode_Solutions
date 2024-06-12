class Solution {
public:
    string removeKdigits(string num, int k) {
        stack<char> stack;
        for(char d: num) {
            while(!stack.empty() && k > 0 && stack.top() > d) {
                stack.pop();
                k--;
            }
            stack.push(d);
        }

        while(k > 0  && !stack.empty()) {
            stack.pop();
            k--;
        }

        string res;
        while(!stack.empty()){
            res += stack.top();
            stack.pop();
        }
        reverse(res.begin(), res.end());
        size_t pos = res.find_first_not_of('0');
        res = (pos == string::npos? "0" : res.substr(pos));
        return res;
    }
};