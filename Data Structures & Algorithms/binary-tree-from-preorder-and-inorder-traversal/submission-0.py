# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder is None or len(preorder) == 0:
            return None

        locs = {val: idx for idx,val in enumerate(inorder)}

        self.i = 0
        def build_helper(l, r):
            if l > r:
                return None

            root_val = preorder[self.i]
            self.i+=1
            root = TreeNode(root_val)
            root_loc = locs[root_val]

            root.left = build_helper(l, root_loc - 1)
            root.right = build_helper(root_loc + 1, r)
            return root

        return build_helper(0, len(inorder) - 1)

        