class Node:

    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return self.__str__()


class Tree:
    def __init__(self):
        self.root: Node = None
        self.index = -1

    def _build_tree(self, pre_order_seq):
        self.index += 1
        ele = pre_order_seq[self.index]

        if ele == -1:
            return None

        root = Node(data=ele)
        root.left = self._build_tree(pre_order_seq)
        root.right = self._build_tree(pre_order_seq)
        return root

    def build_tree(self, pre_order_seq: list):
        self.root = self._build_tree(pre_order_seq)
        return self

    def _pre_order_traverse(self, root: Node):

        if root is None:
            return

        print(root.data)
        self._pre_order_traverse(root.left)
        self._pre_order_traverse(root.right)
        return

    def pre_order_traverse(self):
        self._pre_order_traverse(self.root)
        print("-----------------")
        return self

    def _in_order_traverse(self, root: Node):

        if root is None:
            return

        self._in_order_traverse(root.left)
        print(root.data)
        self._in_order_traverse(root.right)

    def in_order_traverse(self):
        self._in_order_traverse(self.root)
        print("-----------------")
        return self

    def _post_order_traverse(self, root: Node):

        if root is None:
            return

        self._post_order_traverse(root.left)
        self._post_order_traverse(root.right)
        print(root.data)

    def post_order_traverse(self):
        self._post_order_traverse(self.root)
        print("-----------------")
        return self

    def level_order(self):
        from collections import deque

        queue = deque()
        root = self.root
        queue.append(root)

        while queue:

            ele = queue.popleft()
            print(ele.data)

            if ele.left:
                queue.append(ele.left)

            if ele.right:
                queue.append(ele.right)
        print("-----------------")

        return self

    def height_of_tree(self, root: Node):
        if not root:
            return 0

        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)

        return 1 + max(left_height, right_height)

    def count_nodes(self, root: Node):

        if not root:
            return 0

        left_height = self.count_nodes(root.left)
        right_height = self.count_nodes(root.right)

        return 1 + left_height + right_height

    def count_leaf_nodes(self, root: Node):

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left_height = self.count_leaf_nodes(root.left)
        right_height = self.count_leaf_nodes(root.right)

        return left_height + right_height

    def _is_tree_balanced(self, root: Node):

        if not root:
            return 0, True

        left_height, is_left_balance = self._is_tree_balanced(root.left)
        right_height, is_right_balance = self._is_tree_balanced(root.right)

        current_height = 1 + max(left_height, right_height)

        is_current_balanced = (
            is_left_balance
            and is_right_balance
            and abs(left_height - right_height) <= 1
        )

        return current_height, is_current_balanced

    def is_tree_balanced(self):
        if not self.root or (not self.root.left and not self.root.right):
            return True

        _, is_balanced = self._is_tree_balanced(self.root)
        return is_balanced

    def mirror_tree(self, root: Node):
        if not root:
            return None

        self.mirror_tree(root.left)
        self.mirror_tree(root.right)

        root.left, root.right = root.right, root.left

    def level_order_with_line(self):
        print("\n\n")
        from collections import deque

        queue: deque[Node] = deque()
        root = self.root

        queue.append(root)
        queue.append(None)

        while queue:

            node = queue.popleft()

            if node is None:

                if not queue:
                    break

                print("\n")
                queue.append(None)
                continue

            print(str(node) + " ", end="")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print("\n\n")

    def identical_tree(self, root1: Node, root2: Node):

        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        is_identical1 = self.identical_tree(root1.left, root2.left)
        is_identical2 = self.identical_tree(root1.right, root2.right)

        return is_identical1 and is_identical2 and root1.data == root2.data

    def diameter_of_tree(self, root: Node):

        if not root:
            return 0

        left_diameter = self.diameter_of_tree(root.left)
        right_diameter = self.diameter_of_tree(root.right)

        left_h = self.height_of_tree(root.left)
        right_h = self.height_of_tree(root.right)

        return max(left_diameter, right_diameter, left_h + right_h)


if __name__ == "__main__":

    pre_order_seq = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]

    tree = Tree()
    tree.build_tree(pre_order_seq)

    tree2 = Tree()
    tree2.build_tree(pre_order_seq)

    print("identical_tree >> ", tree2.identical_tree(tree.root, tree2.root))
    # .pre_order_traverse().in_order_traverse().post_order_traverse().level_order().height_of_tree()

    # print("height_of_tree>> ", tree.height_of_tree(tree.root))
    # print("count_nodes>>    ", tree.count_nodes(tree.root))
    # print("count_leaf_nodes>>    ", tree.count_leaf_nodes(tree.root))
    # print("is_tree_balanced>>    ", tree.is_tree_balanced())
    # tree.mirror_tree(tree.root)
    # tree.level_order_with_line()
