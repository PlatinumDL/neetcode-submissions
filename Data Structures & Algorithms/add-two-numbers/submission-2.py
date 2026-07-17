# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Create a new LL from the sum of each node in both LLs
        #If a sum is larger than 10, modulo it by 10 and store it instead. Then, add 1 to the next sum.
        
        cur1 = l1
        cur2 = l2
        prev = 0
        newHead = ListNode()
        curNew = newHead

        while cur1 and cur2:
            summed = cur1.val + cur2.val + prev
            #If summed >= 10
            if summed >= 10:
                newVal = summed % 10
                prev = 1
                newNode = ListNode(newVal)
                curNew.next = newNode
                curNew = curNew.next
            else:
                prev = 0
                newNode = ListNode(summed)
                curNew.next = newNode
                curNew = curNew.next
            cur1 = cur1.next
            cur2 = cur2.next
        
        while cur1:
            summed = cur1.val + prev

            if summed >= 10:
                newVal = summed % 10
                prev = 1
                newNode = ListNode(newVal)
                curNew.next = newNode
                curNew = curNew.next
            else:
                prev = 0
                newNode = ListNode(summed)
                curNew.next = newNode
                curNew = curNew.next

            cur1 = cur1.next
        while cur2:
            summed = cur2.val + prev
            
            if summed >= 10:
                newVal = summed % 10
                prev = 1
                newNode = ListNode(newVal)
                curNew.next = newNode
                curNew = curNew.next
            else:
                prev = 0
                newNode = ListNode(summed)
                curNew.next = newNode
                curNew = curNew.next
                
            cur2 = cur2.next
        
        #Remaining 1
        if prev == 1:
            curNew.next = ListNode(1)
        
        return newHead.next