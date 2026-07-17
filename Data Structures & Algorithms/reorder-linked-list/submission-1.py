# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Go until the mid point -> then split it out into another linkedList
        #From the new LL, attach a note inbetween every node in the earlier linked list

        #Get Length of LL
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        #Get midpoint of LL
        mid = length // 2

        #Traverse to mid
        cur = head
        counter = 0
        while counter < mid:
            cur = cur.next
            counter += 1
        
        #Save mid point and cut off .next of previous LL
        midPoint = cur.next
        cur.next = None

        #Reverse mid point LL
        prev = None
        cur = midPoint

        while cur:
            #Save next to variable
            nextTemp = cur.next
            #Reverse -> point next to previous
            cur.next = prev
            #Update Prev
            prev = cur
            #Move current to next
            cur = nextTemp
        
        newHead = prev #New head of LL

        #Now, combine the two LLs
        cur = head
        while newHead:
            #Save newHead.next to this var
            attachTo = cur.next
            #Attach
            cur.next = newHead
            #Save new head
            temp = newHead.next
            #Attach
            newHead.next = attachTo
            #Update new Head
            newHead = temp
            #Update cur 
            cur = attachTo