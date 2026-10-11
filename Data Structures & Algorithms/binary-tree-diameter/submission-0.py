# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(root):
            if not root:
                return 0

            l_depth = dfs(root.left)
            r_depth = dfs(root.right)

            self.res = max(self.res, l_depth + r_depth)

            return 1 + max(l_depth, r_depth)
        
        dfs(root)

        return self.res
        
        