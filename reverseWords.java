class Solution {
    String[] words;
    public String reverseWords(String s) {
        
        words=s.trim().split("\\s+");

        StringBuilder sb = new StringBuilder("");

        for (int i=words.length-1; i>0; i--) {
            sb.append(words[i]);
            sb.append(" ");
        }
        sb.append(words[0]);
        return sb.toString();
    }
}
