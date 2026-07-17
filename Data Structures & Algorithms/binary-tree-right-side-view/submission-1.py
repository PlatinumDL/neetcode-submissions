# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        output = []
        queue.append(root)

        if root == None:
            return output
            
        #BFS -> add the ones all the way on the right to the list
        while len(queue) > 0:
            last = len(queue)
            for i in range(len(queue)):
                temp = queue.popleft()
                if i == last-1: #Last from the right side, add to output
                    output.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        
        return output
        