# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_helper(node, left, right):
            if node is None:
                return True

            if not (left < node.val < right):
                return False

            return validate_helper(node.left, left, node.val) and validate_helper(
                node.right, node.val, right)

        return validate_helper(root, float("-inf"), float("inf"))

