class Solution {
public:
    int appendCharacters(string s, string t) {
        int count=0;
        for (auto ch:s){
            if (ch==t[count]) count++;
            
        }
        return t.length()-count;
        
    }
};
