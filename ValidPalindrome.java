class Solution {
    public boolean isPalindrome(String s) {
        int ptr1=0;
        s=s.toLowerCase().replaceAll("[^a-z0-9]","");
        int ptr2=s.length()-1;
        String[] strArr = s.split("");
        if(strArr.length<=1){
            return true;
        }
        for(String str: strArr) {
            if(str.equals(strArr[ptr2-ptr1])){
                ptr1+=1;
                continue;
            }
            else {
                return false;
            }
        }
        return true;
    }
}
