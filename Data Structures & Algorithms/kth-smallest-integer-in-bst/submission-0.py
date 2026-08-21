class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        count = k

        def dfs(node):
            nonlocal count, ans

            if not node:
                return

            dfs(node.left)

            count -= 1
            if count == 0:
                ans = node.val
                return

            dfs(node.right)

        dfs(root)
        return ans