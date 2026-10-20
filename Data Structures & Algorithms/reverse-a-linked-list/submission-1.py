# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# recursive solution 
# might want to retry, kind of hard to wrap head around

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use natural flow of recursion to reverse the pointers
        # go to the end of the ListNode
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead