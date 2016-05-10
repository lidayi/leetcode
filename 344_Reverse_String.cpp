class Solution {
public:
    string reverseString(string s) {
        int t = s.length();
        char a;
        for(int i = 0; i < t/2; i++){
            a = s[i];
            s[i] = s[t-1-i];
            s[t-1-i] = a;
        }
        return s;
    }
};
