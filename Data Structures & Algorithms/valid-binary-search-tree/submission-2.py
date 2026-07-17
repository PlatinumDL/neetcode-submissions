# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.output = True

        #Upper Bound -> cannot be higher than this, initially it is the root
        def dfs(node, upper, lower):
            if node == None:
                return
            
            #Invalid -> cannot be larger than upper bound
            if upper != None and node.val >= upper:
                self.output = False
            #Invalid -> cannot be lower than lower bound
            if lower != None and node.val <= lower:
                self.output = False

            #Left tree, cannot be higher than node.val
            dfs(node.left,node.val,lower)
            #Right tree, cannot be lower than node.val
            dfs(node.right,upper,node.val)


        dfs(root.left, root.val, None)
        dfs(root.right, None, root.val)
        return self.output
        