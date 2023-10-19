class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_left_leaves(root):
    if root is None:
        return

    stack = [root]
    left_leaves = []
    left_leaves_sum = 0

    while stack:
        node = stack.pop()

        if node.right:
            stack.append(node.right)

        if node.left:
            if not node.left.left and not node.left.right:
                left_leaves.append(node.left.value)
                left_leaves_sum += node.left.value
            stack.append(node.left)

    if left_leaves:
        print("Значення лівих листків:", left_leaves)

    return left_leaves_sum

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
# root.left.left = TreeNode(14)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)
print((print_left_leaves(root)))
