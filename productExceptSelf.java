import java.util.*;
class Solution {
    public int[] productExceptSelf(int[] nums) {
        boolean zeroFlag=false;
        int[] answer=new int[nums.length];
        int product=1;
        int zeroCount=0;
        for (int i=0; i<nums.length; i++) {
            if (nums[i]==0) {
                zeroCount+=1;
                continue;
            }
            product*=nums[i];
        }
        for (int i=0; i<nums.length; i++) {
            if (nums[i]==0) {
                if (zeroCount<2)
                    answer[i]=product;
                else
                    answer[i]=0;
            }
            else{
                if (zeroCount==0)
                    answer[i]=product/nums[i];
                else
                    answer[i]=0;
            }           
        }
        return answer;
    }
}
