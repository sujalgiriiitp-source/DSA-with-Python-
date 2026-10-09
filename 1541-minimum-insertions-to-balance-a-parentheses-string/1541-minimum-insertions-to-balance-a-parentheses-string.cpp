class Solution {
public:
    int minInsertions(string s) {
        int res = 0, right = 0;
        for (char c : s) {
            if (c == '(') {
                if (right % 2 != 0) res++, right--;
                right += 2;
            } else {
                if (--right < 0) res++, right += 2;
            }
        }
        return res + right;
    }
};