# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root.left and not root.right:
            return True

        if not root.left and root.right:
            return False

        if root.left and not root.right:
            return False

        def is_same(p: TreeNode, q: TreeNode):

            if not p and not q:
                return True

            if p and not q:
                return False

            if not p and q:
                return False

            if p.val != q.val:
                return False

            if not is_same(p.left, q.right):
                return False

            if not is_same(p.right, q.left):
                return False

            return True

        return is_same(root.left, root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)


print(Solution().isSymmetric(root))
