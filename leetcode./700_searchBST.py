class Solution:
    def searchBSTRecursively(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBSTRecursively(root.left, val)
        else:
            return self.searchBSTRecursively(root.right, val)
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.searchBSTRecursively(root, val)
            
