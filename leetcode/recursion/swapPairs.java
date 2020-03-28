
public class Test {
    public static ListNode swapPairs(ListNode head) {
    	if(head!=null && head.next!=null) {
	    	int temp = head.val;
	    	head.val = head.next.val;
	    	head.next.val = temp;
	    	
	    	swapPairs(head.next.next);
    	}
    	return head;
    }
	
	public static void main(String[] args) {
		ListNode head = new ListNode(1);
		head.next = new ListNode(2);
		head.next.next = new ListNode(3);
		head.next.next.next = new ListNode(4);
		
		printList(head);
		System.out.println();
		swapPairs(head);
		printList(head);
	}
	
	public static void printList(ListNode head) {
		ListNode pointer = head;
		while(pointer!=null) {
			System.out.print(pointer.val+" ");
			pointer = pointer.next;
		}
	}
}
