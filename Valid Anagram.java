import java.util.*;
class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> hashMap = new HashMap<String, Integer>();
        if(s.length()!=t.length()){
            return false;
        }
        for(String i: t.split("")){
            if(!hashMap.containsKey(i)){
                hashMap.put(i,1);
            }
            else {
                hashMap.put(i,hashMap.get(i)+1);
            }
        }
        for(String j: s.split("")){
            if (!hashMap.containsKey(j)){
                return false;
            }
            else{
                hashMap.put(j,hashMap.get(j)-1);
            }
        }
        for (Map.Entry<String,Integer> entry : hashMap.entrySet()){
            if(entry.getValue()!=0){
                return false;
            }
        }
        return true;
    }
}

