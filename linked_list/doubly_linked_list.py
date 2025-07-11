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

        self.length += 1
        if self.head is None:
            self.head = Node(data=data)
            return self

        head = self.head
        new_node = Node(data=data)

        new_node.next_node = head
        head.prev_node = new_node
        self.head = new_node
        return self

    def display(self):
        node = self.head

        result = []
        while node:

            node_data = f"{str(node)}"
            result.append(node_data)

            node = node.next_node

        print(" <-> ".join(result))
        return self

    def reverse_ll(self):
        if self.head is None:
            raise ValueError("Empty List")

        current = self.head
        prev_node = None

        while current is not None:
            temp = current.next_node

            current.next_node = current.prev_node
            current.prev_node = temp

            prev_node = current
            current = temp

        self.head = prev_node
        return self

    def delete(self):

        if self.head is None:
            return self

        return self


if __name__ == "__main__":
    link_list_head = LinkList()

    link_list_head.insert_at_end(10).insert_at_end(20).insert_at_end(
        30
    ).insert_at_start(0).reverse_ll().display()
