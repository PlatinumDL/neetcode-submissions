# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Depth on both sides should not differ by more than 1
        self.output = True

        def dfs(node, depth):
            if node == None:
                return depth

            leftDepth = dfs(node.left, depth)
            rightDepth = dfs(node.right, depth)
            
            if abs(leftDepth - rightDepth) > 1:
                self.output = False

            depth = max(leftDepth,rightDepth)
            return depth+1

        dfs(root,0)
        
        return self.output