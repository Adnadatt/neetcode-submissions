# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# use stack, read all the values, and then pop off the top to make a new ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        curr = head

        while curr:
            list.append(curr.val)
            curr = curr.next

        dummy = ListNode()
        tail = dummy

        while list:
            tail.next = ListNode(list.pop())
            tail = tail.next

        return dummy.next