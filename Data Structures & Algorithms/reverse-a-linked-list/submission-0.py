# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        prev = None
        cur = head

        while cur:
            #Get next placeholder
            tempnext = cur.next
            #Update cur next with previous (reverse)
            cur.next = prev
            #Update previous with cur
            prev = cur
            #Move cur to tempnext
            cur = tempnext

        head = prev
        
        return head