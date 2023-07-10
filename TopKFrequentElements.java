import java.util.*;
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> hashMap= new HashMap<>();
        for(int no:nums) {
            if(hashMap.containsKey(no)) {
                hashMap.put(no,hashMap.get(no)+1);
            }
            else{
                hashMap.put(no,1);
            }   
        }
      
        LinkedHashMap<Integer, Integer> sortedMap = new LinkedHashMap<>();
        hashMap.entrySet().stream()
                .sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed())
                .forEachOrdered(entry -> sortedMap.put(entry.getKey(), entry.getValue()));
        
        List<Integer> soln = new ArrayList<Integer>();
        int count=0;
        for (Map.Entry<Integer, Integer> entry : sortedMap.entrySet()) {
            if(count<k){
                soln.add(entry.getKey());
            }
            count++;
        }
        // System.out.println(soln);
        return soln.stream().mapToInt(Integer::intValue).toArray();
           
    }
}
