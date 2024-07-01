class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def convert(head):
    if not head:
        return None
    
    root = TreeNode(head.val)
    queue = [root]
    head = head.next
    
    while head:
        parent = queue.pop(0)
        
        leftChild = TreeNode(head.val)
        parent.left = leftChild
        queue.append(leftChild)
        head = head.next
        
        if head:
            rightChild = TreeNode(head.val)
            parent.right = rightChild
            queue.append(rightChild)
            head = head.next
            
    return root
