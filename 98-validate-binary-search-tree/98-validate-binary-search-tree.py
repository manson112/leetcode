# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validLeftBST(self, root: Optional[TreeNode], maxValue: int, minValue: int) -> bool:
        if root == None:
            return True
        print("left// maxValue = ", maxValue, ", minValue = ", minValue)
        print(root.val)
        result = self.validLeftBST(root.left, root.val, minValue) and self.validRightBST(root.right, maxValue, root.val)
        if minValue != None:
            result = result and root.val > minValue
        return result and root.val < maxValue 
    
    def validRightBST(self, root: Optional[TreeNode], maxValue: int, minValue: int) -> bool:
        if root == None:
            return True
        print("right// maxValue = ", maxValue, ", minValue = ", minValue)
        print(root.val)
        result = self.validLeftBST(root.left, root.val, minValue) and self.validRightBST(root.right, maxValue, minValue)
        if maxValue != None:
            result = result and root.val < maxValue
        return result and root.val > minValue
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validLeftBST(root.left, root.val, None) and self.validRightBST(root.right, None, root.val)