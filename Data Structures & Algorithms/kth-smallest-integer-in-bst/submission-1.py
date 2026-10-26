# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        def inOrder(root):
            if not root:
                return None
            
            inOrder(root.left)
            self.arr.append(root.val)
            inOrder(root.right)
            
            return

        inOrder(root)
        
        return self.arr[k - 1]



        