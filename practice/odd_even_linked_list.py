class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head

        head1=head
        head2,head2_beg= head.next,head.next
        while head2.next!= None and head2.next.next!= None:
            head1.next = head2.next
            head2.next = head2.next.next
            head1 = head1.next
            head2 = head2.next

        if head2.next!=None:
            head1.next = head2.next
            head1 = head1.next
        head1.next = head2_beg
        head2.next = None
        return head
    
    def print(self, head):
        node = head
        while node:
            print(node.val)
            node = node.next



if __name__ == "__main__":
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five= ListNode(5)    
    one.next = two
    two.next =  three
    three.next = four
    four.next = five


    c  = Solution()

    d = c.oddEvenList(one)

    c.print(d)

    
    
