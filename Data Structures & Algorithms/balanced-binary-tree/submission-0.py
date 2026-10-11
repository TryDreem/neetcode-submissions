# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balanced = True

        def goDepth(root):
            if root is None:
                return 0

            l_depth = goDepth(root.left)
            r_depth = goDepth(root.right)

            if abs(l_depth - r_depth) > 1:
                    self.balanced = False

            return 1 + max(l_depth, r_depth)

        goDepth(root)

        return self.balanced