# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.output = 0

        def dfs(node, path):
            if node == None:
                return

            #check path
            check = True
            #Check if any previous nodes are larger
            for i in path:
                if i > node.val:
                    check = False
            
            #Increment good node value
            if check:
                self.output += 1
            path.append(node.val)
            
            dfs(node.left, path.copy())
            dfs(node.right, path.copy())

        dfs(root,[])
        return self.output
        