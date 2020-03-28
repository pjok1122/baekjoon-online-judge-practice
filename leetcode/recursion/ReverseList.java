/*
    단방향 LinkedList가 주어져있다.
    홀수 번째에만 인접한 두 리스트 노드 간에 스왑을 진행한다. 
    
    1->2->3->4->5->6
    
    2->1->4->3->6->5 로 바꾸고 헤드를 리턴하는 메서드를 생성하라.
*/


// 1. 재귀를 어떻게 호출할 것인가.
// 2. 언제 재귀를 종료할 것인가. (제일 중요)
// 3. 재귀가 종료되었다고 했을 때, (마지막 리커전부터 뒤로 생각) 무슨 일을 행해야 하는가.

public class ReverseList {
	
	/*
	 * 
	 * Input: 1->2->3->4->5->NULL
		Output: 5->4->3->2->1->NULL
	 */
	
	public static ListNode reverseList(ListNode head) {
		if(head==null) {
			return null;
		}
		if(head.next==null) {
			return head;
		}

		//새로운 헤드를 반환하기 위해 위치를 찾는다.
		ListNode pointer = head;
		while(pointer.next!=null){
			pointer = pointer.next;
		}

		//재귀를 시작하기 전에 할 행동. 1을 가리키고 있는 상황.
		
		reverseList(head.next);

		//재귀가 끝난 상황에서 출발. 5를 가리키고 있는 상황.
		head.next.next = head;
		head.next = null;
		
		return pointer;
	}
	
	public static ListNode swapListNode(ListNode head) {
		if(head==null || head.next == null) {
			return null;
		}
		
		int temp = head.val;
		head.val = head.next.val;
		head.next.val = temp;
		
		swapListNode(head.next.next);
		
		return head;
	}
	
//	public static void main(String[] args) {
//		//2->10->4->3->5->6
//		ListNode head = listNodeConstructor();
//		ListNode head2 = reverseList(head);
//		
//		printListNode(head2);
//	
//	}

	private static ListNode listNodeConstructor() {
		ListNode head = new ListNode(2);
		head.next = new ListNode(10);
		head.next.next = new ListNode(4);
		head.next.next.next = new ListNode(3);
		head.next.next.next.next = new ListNode(5);
		head.next.next.next.next.next = new ListNode(6);
		
		return head;
	}
	
	public static void printRecursive(ListNode head) {
		if(head==null) {
			return ;
		}
		printRecursive(head.next);
		System.out.print(head.val+" -> ");
	}
	
	public static void printListNode(ListNode head) {
		ListNode pointer = head;
		while(pointer!=null) {
			System.out.print(pointer.val+"-> ");
			pointer = pointer.next;
		}
		
		System.out.println();
	}
	
}


class ListNode {
	int val;
	ListNode next;
	ListNode(int x) { val = x; }
}