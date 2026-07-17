# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #set new head, then traverse list
        if list1 and list2 and list1.val <= list2.val:
            head = list1
            list1 = list1.next
        elif list1 and list2 and list1.val > list2.val:
            head = list2
            list2 = list2.next
        elif list1:
            head = list1
            list1 = list1.next
        elif list2:
            head = list2
            list2 = list2.next
        else:
            return list1
        
        #Cur represents the merged list
        cur = head
        
        #While both lists are present, compare and add
        while list1 and list2:
            if list1.val <= list2.val: #List1 is smaller, add to head/cur, then traverse
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next


        #Clear remaning elements -> add to cur
        while list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next

        while list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
        
        return head

        