class Solution:
    
    def isMirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
