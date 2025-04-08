class Solution {
    public boolean isSubsequence(String s, String t) {
        int i=0;
        int j=0;
        if (s.length()==0) {
            return true;
        }
        while(j<t.length()){
            if (i<s.length() && s.charAt(i)==t.charAt(j)){
                i+=1;
            }
            j+=1;
        }
        if (i==s.length()) return true;
        else return false;
        
    }
}
