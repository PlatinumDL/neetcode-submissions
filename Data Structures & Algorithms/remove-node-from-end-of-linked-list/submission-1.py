# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Get length of LL, then calculate where to pop
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        #Where to pop
        difference = length - n
        #If difference is 0, pop from head of list
        if difference == 0:
            return head.next

        #Traverse to difference
        cur = head
        counter = 1
        while cur and counter < difference:
            cur = cur.next
            counter += 1
        
        print(cur.val)
        attachTo = cur.next.next
        cur.next = attachTo
        
        return head