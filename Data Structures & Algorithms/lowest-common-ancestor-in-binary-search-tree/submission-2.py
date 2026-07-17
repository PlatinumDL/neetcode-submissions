# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #DFS -> When p OR q is found, set it to ancestor -> then continue DFS to find the OTHER one. If not found, back track and until other one is found
        #Topmost ancestor
        ancestor = root

        while True:
            if ancestor.val < p.val and ancestor.val < q.val: #Both in right subtree
                ancestor = ancestor.right
                continue

            if ancestor.val > p.val and ancestor.val > q.val: #Both in left subtree
                ancestor = ancestor.left 
                continue

            if ancestor.val > p.val and ancestor.val < q.val:
                return ancestor
            if ancestor.val < p.val and ancestor.val > q.val:
                return ancestor
            
            #Keep Traversing until the conditions above are no longer true
            if ancestor.val == p.val:
                return p
            if ancestor.val == q.val:
                return q

        return ancestor
        