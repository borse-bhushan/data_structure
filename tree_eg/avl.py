class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return self.__str__()


class AVLTree:

    def __init__(self):
        self.root: Node = None

    def _insert(self, node: Node, data_node: Node):
        if node.data == data_node.data:
            raise ValueError("Already Exist")

        if node.data < data_node.data:
            if node.right is None:
                node.right = data_node
                return
            self._insert(node.right, data_node)
        else:
            if node.left is None:
                node.left = data_node
                return
            self._insert(node.left, data_node)

    def insert(self, data):

        node = Node(data)
        if self.root is None:
            self.root = node
            return self

        self._insert(self.root, node)
        return self

    def height_of_tree(self, root: Node):

        if root is None:
            return 0

        lh = self.height_of_tree(root.left)
        rh = self.height_of_tree(root.right)

        return 1 + max(lh, rh)

    def print_tree(self, root):
        if not root:
            print("Tree is empty")
            return

        height = self.height_of_tree(root)
        width = (2**height) - 1  # Full width for balanced tree
        res = [[" " for _ in range(width)] for _ in range(height)]

        self.fill(res, root, 0, 0, width - 1)

        for row in res:
            print("".join(row))

        return self

    def fill(self, res, node, level, l, r):
        if not node:
            return
        mid = (l + r) // 2
        res[level][mid] = str(node.data)
        self.fill(res, node.left, level + 1, l, mid - 1)
        self.fill(res, node.right, level + 1, mid + 1, r)

    def deleteNode(self, root: Node, node_data):

        if root is None:
            return None

        if root.data < node_data:
            root.right = self.deleteNode(root.right)
        elif root.data > node_data:
            root.left = self.deleteNode(root.right)
        else:

            if root.left is None and root.right is None:
                del root
                return None

            if root.right:
                pass

            current = root.right or root.left
            while current and current.right:
                current = current


if __name__ == "__main__":
    avl_tree = AVLTree()

    avl_tree.insert(30).insert(50).insert(40).insert(70).insert(60).insert(10).insert(
        20
    ).insert(5).print_tree(avl_tree.root).deleteNode(avl_tree.root, 50)

    # print(avl_tree.height_of_tree(avl_tree.root))
#  * level
