class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None


class BST:
    def __init__(self):
        self.root: Node = None

    def _insert(self, root: Node, data: int):

        if root.data > data:
            if root.left is None:
                root.left = Node(data=data)
            else:
                self._insert(root.left, data)

        else:
            if root.right is None:
                root.right = Node(data=data)
            else:
                self._insert(root.right, data)

    def insert(self, data: int):

        if not self.root:
            self.root = Node(data=data)
            return self

        self._insert(self.root, data)

        return self

    def _search(self, root: Node, data: int):

        if not root:
            return False

        if root.data == data:
            return True

        if self._search(root.left, data):
            return True

        if self._search(root.right, data):
            return True

        return False

    def min_value(self, root: Node):

        if root is None:
            return float("inf")

        left_min = self.min_value(root.left)
        right_min = self.min_value(root.right)

        return min(root.data, left_min, right_min)

    def max_value(self, root: Node):

        if root is None:
            return float("-inf")

        left_max = self.max_value(root.left)
        right_max = self.max_value(root.right)

        return max(root.data, left_max, right_max)

    def search(self, data: int):
        if self.root is None:
            return False
        return self._search(self.root, data)

    def is_valid_bst(self, root):

        if root is None:
            return True
        pass


if __name__ == "__main__":
    bst = BST()

    bst.insert(data=10).insert(data=20).insert(5)

    # print(bst.min_value(bst.root))
    # print(bst.max_value(bst.root))
    print(bst.is_valid_bst(bst.root))
