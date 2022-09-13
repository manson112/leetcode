# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findMaxDepth(root: Optional[TreeNode], depth:int) -> int:
            if root == None:
                return depth
            return max(findMaxDepth(root.left, depth+1), findMaxDepth(root.right, depth+1))
        
        return findMaxDepth(root, 0)
            