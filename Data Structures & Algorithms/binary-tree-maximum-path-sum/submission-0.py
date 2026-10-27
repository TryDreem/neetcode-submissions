# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            maxLeft = max(left, 0)
            maxRight = max(right, 0)
            split = root.val + maxLeft + maxRight
            self.res = max(self.res, split)
            return root.val + max(maxLeft, maxRight)

        dfs(root)
        return self.res
