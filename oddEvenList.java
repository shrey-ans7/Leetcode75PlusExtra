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
class Solution {
    ListNode oddIter, evenHead, evenIter;
    public ListNode oddEvenList(ListNode head) {
        if (head==null || head.next==null) return head;
        oddIter=head; evenHead=head.next; evenIter=evenHead;
        while(evenIter!=null && evenIter.next!=null) {
            oddIter.next=evenIter.next;
            oddIter=oddIter.next;
            evenIter.next=evenIter.next.next;
            evenIter=evenIter.next;
        }
        oddIter.next=evenHead;
        return head;
        
    }
}
