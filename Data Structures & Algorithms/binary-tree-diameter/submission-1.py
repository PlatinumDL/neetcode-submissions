# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        #Largest Diameter = longest depth of left + longest depth of right
        self.getDepth(root, 0)
        return self.maxDiameter

    def getDepth(self, root, depth):
        if root == None:
            return depth
        
        depthL = self.getDepth(root.left,depth)
        depthR = self.getDepth(root.right,depth)
        newDia = depthL + depthR
        self.maxDiameter = max(newDia, self.maxDiameter)
        depth = max(depthL,depthR)

        return depth+1