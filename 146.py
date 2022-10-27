# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root: Optional[TreeNode], ret: List[int]):
            if root == None:
                return
            l = postorder(root.left, ret)
            if l != None:
                ret += [l]
            r = postorder(root.right, ret)
            if r != None: 
                ret += [r]
            ret += [root.val]

        result = []
        postorder(root, result)
        return result
