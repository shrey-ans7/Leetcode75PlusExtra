import java.util.*;

class Solution {
    String formatString(String str) {
        char charArray[] = str.toCharArray();
        Arrays.sort(charArray);
        return new String(charArray);
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> soln = new ArrayList<>();
        HashMap<String, List<String>> hashMap = new HashMap<>();
        String key = "";
        for (String i : strs) {
            key = formatString(i);
            if (hashMap.containsKey(key)) {
                hashMap.get(key).add(i);
            } else {
                hashMap.put(key, new ArrayList<>(Arrays.asList(i)));
            }
        }
        for (Map.Entry<String, List<String>> entry : hashMap.entrySet()) {
            soln.add(entry.getValue());
        }
        return soln;
    }
}
