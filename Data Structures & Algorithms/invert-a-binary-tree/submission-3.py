# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Recursion -> Go in as far as you can, swap the left and right -> move out and swap the left and right
        #Base Case (Leaf Node)
        if root == None:
            return root

        if root.left != None or root.right != None:
            left = root.left
            right = root.right
            root.right = left
            root.left = right

            #Run invert tree on subnodes (if not none)
            self.invertTree(root.left)
            self.invertTree(root.right)
            
        return root
        