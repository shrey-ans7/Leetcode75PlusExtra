class Solution {
    String vowels = "aeiouAEIOU";
    char[] chars;
    public String reverseVowels(String s) {
        chars = s.toCharArray();
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            while(left<right && vowels.indexOf(chars[left])==-1) {
                left+=1;
            }
            while(right>left && vowels.indexOf(chars[right])==-1) {
                right-=1;
            }
            char swap = chars[left];
            chars[left]=chars[right];
            chars[right]=swap;
            left+=1;
            right-=1;
        }
        s = new String(chars);
        return s;

        
    }
}
