# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p == None and q == None:
            return True
        
        if p != None and q != None and p.val == q.val:
                if self.isSameTree(p.left,q.left) == False:
                    return False
                if self.isSameTree(p.right,q.right) == False:
                    return False
                return True

        return False



