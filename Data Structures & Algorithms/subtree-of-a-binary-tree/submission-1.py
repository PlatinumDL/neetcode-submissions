# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.output = False    
        
        def compareDFS(node, subroot):
            if node == None and subroot == None:
                return True
            if node != None and subroot != None and node.val == subroot.val:
                if compareDFS(node.left, subroot.left) == True and compareDFS(node.right, subroot.right) == True:
                    return True
            
            return False

        def dfs(node):
            if node == None:
                return
            
            if compareDFS(node,subRoot) == True:
                self.output = True

            dfs(node.right)
            dfs(node.left)

        dfs(root)
        return self.output
        