class Solution:
        
    def minDiffInBST(self, root: TreeNode) -> int:
        self.prev = float('-inf')
        self.min = float('inf')
        
        def recursive(root):
            if root:
                recursive(root.left)
                self.min = min(self.min, root.val - self.prev)
                self.prev = root.val
                recursive(root.right)
        recursive(root)
        return self.min
