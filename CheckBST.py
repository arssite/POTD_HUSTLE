class Solution:
    def __init__(self):
        self.temp = []
    
    def isBST(self, root):
        self.inorder(root)
        
        # Check if temp list is sorted
        for i in range(1, len(self.temp)):
            if self.temp[i] <= self.temp[i - 1]:
                return False
        
        return True
    
    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        self.temp.append(root.data)
        self.inorder(root.right)
