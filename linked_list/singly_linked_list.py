class Node:

    def __init__(self, data):
        self.data = data
        self.next_node: Node = None

    def __str__(self):
        return f"{self.data}"


class LinkList:
    def __init__(self):
        self.head: Node = None

    def insert_at_end(self, data):

        if self.head is None:
            self.head = Node(data=data)
            return self

        current_node: Node = self.head

        while current_node.next_node is not None:
            current_node: Node = current_node.next_node

        current_node.next_node = Node(data=data)

        return self

    def insert_at_start(self):
        pass

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
    link_list_head.insert_at_end(10).insert_at_end(20).insert_at_end(30).display()
