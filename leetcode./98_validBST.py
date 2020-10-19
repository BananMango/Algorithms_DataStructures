class Solution:
    def isValidBSTRecursive(self, node, min_value, max_value):
        if node is None:
            return True
        if min_value is not None and node.val <= min_value:
            return False
        if max_value is not None and node.val >= max_value:
            return False
        
        return (self.isValidBSTRecursive(node.left, min_value, node.val) and 
                self.isValidBSTRecursive(node.right, node.val, max_value))
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTRecursive(root, None, None)
