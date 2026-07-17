"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Use a dictionary corresponding to the value, to store if it is seen before, val is the key
        copyDict = {}

        #Traverse original LL and create new nodes + add to dict
        cur = head
        while cur:
            newNode = Node(cur.val)
            copyDict[cur] = newNode
            cur = cur.next
        
        #With the dictionary, go through the original LL again and update the next and random pointers
        cur = head
        while cur:
            curNode = copyDict[cur]
            #if cur has a next, copy it
            if cur.next != None:
                nextNode = copyDict[cur.next]
                curNode.next = nextNode
            #if cur has a random, copy it
            if cur.random != None:
                randomNode = copyDict[cur.random]
                curNode.random = randomNode
            cur = cur.next

        if head == None:
            return head
        newHead = copyDict[head]
        return newHead