# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 1
        self.arr = []

        def dfs(node):
            if node == None:
                return
            
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return self.arr[k-1]
        