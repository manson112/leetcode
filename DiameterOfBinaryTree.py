# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = 0
    
    def findDepth(self, target: Optional[TreeNode]):
        if target == None:
            return 0
        l = self.findDepth(target.left)
        r = self.findDepth(target.right)
        self.d = max(self.d, l + r)
        return max(l, r) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.findDepth(root)
        return self.d
             
        
