class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal prev, res
            if prev:
                res= min(res, node.val - prev.val)
            prev= node
            dfs(node.right)
        dfs(root)
        return res
