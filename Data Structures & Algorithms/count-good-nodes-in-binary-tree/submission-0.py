# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, currMax):
            if not root:
                return 0
            currMax = max(currMax, root.val)
            left = dfs(root.left, currMax)
            right = dfs(root.right, currMax)
            return 0 + left + right if root.val < currMax else 1 + left + right
        return dfs(root, root.val)
