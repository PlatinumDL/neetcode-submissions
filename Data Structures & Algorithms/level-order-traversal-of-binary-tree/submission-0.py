# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    #BFS, append a list at every level
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        output = []

        if root == None:
            return []
        
        #Put in root first
        queue.append(root)
        
        while len(queue)> 0:
            #For each item in the queue (snapshot, doesnt change)
            subArr = []
            
            for i in range(len(queue)):
                temp = queue.popleft()
                subArr.append(temp.val)
                #append left and right
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

            #Put in subArr
            output.append(subArr)

       
        return output