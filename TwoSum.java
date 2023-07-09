import java.util.Arrays;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] numsOG = nums.clone();
        Arrays.sort(nums);
        int index = -1;
        int[] soln={-1,-1};
        for(int i=0; i<nums.length; i++){
            index = binarySearch(nums, target, nums[i], 0, nums.length-1);
            if(index!=-1){
                if(nums[i]!=nums[index]){
                    for(int k=0; k<numsOG.length; k++) {
                        if(nums[i]==numsOG[k]) {
                            soln[0]=k;
                            break;
                        }
                    }
                    for(int k=0; k<numsOG.length; k++) {
                        if(nums[index]==numsOG[k]) {
                            soln[1]=k;
                            break;
                        }
                    }
                }
                else {
                    int count=0;
                    for(int k=0; k<numsOG.length; k++) {
                        if(nums[index]==numsOG[k] && count == 0) {
                            soln[0]=k;
                            count+=1;
                        }
                        else if(nums[index]==numsOG[k] && count > 0){
                            soln[1]=k;
                            break;
                        }
                    }
                }
                return soln;
            }
        }
        return soln;
    }
    public int binarySearch(int[] nums, int target, int ele, int low, int high){
        int mid = low  + ((high - low) / 2);     
        if (high < low) {
            return -1;
        }
        if (target == nums[mid]+ele) {
            return mid;
        } else if (target < nums[mid]+ele) {
            return binarySearch(nums, target, ele, low, mid - 1);
        } else {
            return binarySearch(nums, target, ele, mid + 1, high);
        }
    }
}
