class Node:

    def __init__(self, data):
        self.data = data
        self.next_node: Node = None

    def __str__(self):
        return f"{self.data}"


class LinkList:
    def __init__(self):
        self.head: Node = None
        self.length = 0

    def insert_at_end(self, data):

        self.length += 1

        if self.head is None:
            self.head = Node(data=data)
            return self

        current_node: Node = self.head

        while current_node.next_node is not None:
            current_node: Node = current_node.next_node

        current_node.next_node = Node(data=data)

        return self

    def insert_at_start(self, data):
        self.length += 1
        new_node = Node(data=data)
        new_node.next_node = self.head
        self.head = new_node
        return self

    def insert_at_index(self, index, data):

        if index == 0:
            self.insert_at_start(data)
            return self

        if index > (self.length + 1) or index < 0:
            raise IndexError(f"The element cant be inserted at {index}")

        if index == (self.length + 1):
            self.insert_at_end(data)
            return self

        self.length += 1

        new_node = Node(data=data)
        current_node = self.head.next_node

        current_index = 0
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

        return self

    def display(self):
        current_node = self.head
        result = []

        while current_node is not None:
            result.append(str(current_node))
            current_node = current_node.next_node

        print(" -> ".join(result) if result else "Empty Linked List")

        return self


if __name__ == "__main__":

    link_list_head = LinkList()
    link_list_head.insert_at_end(10).insert_at_end(20).insert_at_end(
        30
    ).display().insert_at_start(0).display().insert_at_index(
        0, -1
    ).display().insert_at_index(
        6, 40
    ).display().insert_at_index(
        2, 5
    ).display()
