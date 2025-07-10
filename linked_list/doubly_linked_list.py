class Node:

    def __init__(self, data):
        self.data = data
        self.next_node: Node = None
        self.prev_node: Node = None

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return self.__str__()


class LinkList:

    def __init__(self):
        self.head: Node = None
        self.length = 0

    def insert_at_end(self, data):

        self.length += 1

        new_node = Node(data=data)

        if self.head is None:
            self.head = new_node
            return self

        current_node: Node = self.head

        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = new_node
        new_node.prev_node = current_node

        return self

    def insert_at_start(self, data):
        pass

    def display(self):
        node = self.head

        result = []
        while node:

            node_data = f"{str(node)}"

            next_data = f"{str(node.next_node or "")}"
            if next_data:
                next_data = "N-" + next_data + "-> " or ""

            prev_data = f"{str(node.prev_node or "")}"
            if prev_data:
                prev_data = "<-P-" + prev_data or ""

            result.append(f"{prev_data}|C-{node_data}|{next_data}")

            node = node.next_node

        print(" ".join(result))


if __name__ == "__main__":
    link_list_head = LinkList()

    link_list_head.insert_at_end(10).insert_at_end(20).insert_at_end(30).display()
