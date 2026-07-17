# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.output = 0

        def dfs(node, maxVal = None):
            if node == None:
                return


            #Check if any previous nodes are larger
            if maxVal == None or node.val >= maxVal:
                self.output += 1
                maxVal = node.val
            
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root)
        return self.output
        