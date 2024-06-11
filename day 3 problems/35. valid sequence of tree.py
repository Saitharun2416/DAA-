class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidSequence(root, arr):
    def dfs(node, index):
        if not node:
            return False
        if node.val != arr[index]:
            return False
        if index == len(arr) - 1:
            return not node.left and not node.right
        return (node.left and dfs(node.left, index + 1)) or (node.right and dfs(node.right, index + 1))
    
    return dfs(root, 0)
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.left.left.right = TreeNode(1)
root.left.right.left = TreeNode(0)
root.left.right.right = TreeNode(0)

arr = [0, 1, 0, 1]
print(isValidSequence(root, arr)) 

arr = [0, 0, 1]
print(isValidSequence(root, arr)) 

arr = [0, 1, 1]
print(isValidSequence(root, arr))  
