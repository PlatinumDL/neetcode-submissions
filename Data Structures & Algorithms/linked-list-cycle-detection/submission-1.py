# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        cur = head
        
        while cur:
            if seen.get(cur) == None:
                #Not seen, add to dict
                seen[cur] = 1
            else:
                #Seen, return True (cycle exists)
                return True
            #Traverse 
            cur = cur.next
        
        return False
        