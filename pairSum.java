/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.Stack;
class Solution {
    public int pairSum(ListNode head) {
        Stack<Integer> twins = new Stack<>();
        ListNode iter = head;
        while(iter!=null) {
            twins.push(iter.val);
            iter=iter.next;
        }
        iter=head;
        int res=Integer.MIN_VALUE;
        int twin=Integer.MIN_VALUE;
        while(!twins.isEmpty()){
            twin=twins.pop();
            res=Math.max(res,twin+iter.val);
            iter=iter.next;
        }
        return res;
        
    }
}
