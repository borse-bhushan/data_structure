class Node:

    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None


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


if __name__ == "__main__":

    pre_order_seq = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]
    tree = Tree()
    tree.build_tree(
        pre_order_seq
    ).pre_order_traverse().in_order_traverse().post_order_traverse().level_order()
