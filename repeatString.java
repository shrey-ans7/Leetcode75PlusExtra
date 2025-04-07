import java.util.*;
class Solution {
    public static String repeatString(String str, int times) {
        if (times < 0) {
            throw new IllegalArgumentException("Times must be non-negative");
        }
        return str.repeat(times);
    }
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1+str2).equals(str2+str1)) {
            return "";
        }
        int minSize=Math.min(str1.length(),str2.length());
        
        for(int i=minSize; i>0; i--){
            System.out.println(str1.substring(0,i));
            if (str1.length()%i==0 && str2.length()%i==0){
                String cand1 = repeatString(str2.substring(0,i), str1.length()/i);
                String cand2 = repeatString(str1.substring(0,i), str2.length()/i);
                if (cand2.equals(str2) && cand1.equals(str1)) {
                    return cand2.substring(0,i);
                }
            }
            
        }
        return "";
    }

}
