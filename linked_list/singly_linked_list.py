class Node:

    def __init__(self, data):
        self.data = data
        self.next_node: Node = None

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
        if index < 0 or index > self.length:
            raise IndexError(f"The element can't be inserted at index {index}")

        if index == 0:
            return self.insert_at_start(data)

        if index == self.length:
            return self.insert_at_end(data)

        self.length += 1

        new_node = Node(data=data)
        current_node = self.head
        current_index = 0

        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

        return self

    def delete_by_value(self, data):

        if self.head is None:
            raise ValueError("List is empty")

        if self.head.data == data:
            self.head = self.head.next_node
            self.length -= 1
            return self

        prev_node = self.head
        current_node = self.head.next_node

        while current_node is not None:
            if current_node.data == data:
                break

            prev_node = current_node
            current_node = current_node.next_node

        if current_node is None:
            raise ValueError(f"{data} not found")

        prev_node.next_node = current_node.next_node
        self.length -= 1
        return self

    def revers_ll(self):

        if self.head is None:
            raise ValueError("Empty List")

        if self.length == 1:
            return self

        index = 0

        prev = None
        curr = self.head

        while self.length != index:
            index += 1

            nxt = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = nxt

        self.head = prev

        return self

    def find_index(self, data):

        if self.head is None:
            raise ValueError("List is empty")

        if data is None:
            raise ValueError("Cant search none-types")

        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.data == data:
                print(f"Fount at: {index}")
                return self
            index += 1
            current_node = current_node.next_node

        raise ValueError(f"{data} not found in the list")

    def display(self):
        current_node = self.head
        result = []

        while current_node is not None:
            result.append(str(current_node))
            current_node = current_node.next_node

        print(" -> ".join(result) if result else "Empty Linked List")

        return self

    def detect_loop(self):

        visited = {}
        current_node = self.head
        result = []
        index = 0
        while current_node is not None:
            cr_id = id(current_node)
            if cr_id in visited:
                print(f"LOOP DETECTED AT {index}")
                break
            index += 1
            visited[cr_id] = True
            result.append(str(current_node))
            current_node = current_node.next_node

        return self

    def detect_loop_floyd_cycle(self):

        slow = self.head
        fast = self.head

        index = 0
        while fast and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node

            if slow == fast:
                print(f"LOOP DETECTED AT {index}")
                break

            index += 1

        return self


if __name__ == "__main__":

    link_list_head = LinkList()

    a = Node("A")
    link_list_head.head = a

    b = Node("B")
    a.next_node = b

    c = Node("C")
    b.next_node = c

    d = Node("D")
    c.next_node = d

    e = Node("E")
    d.next_node = e

    f = Node("F")
    e.next_node = f

    f.next_node = b

    link_list_head.detect_loop_floyd_cycle()
    link_list_head.detect_loop()

    link_list_head = LinkList()
    link_list_head.insert_at_end(10).insert_at_end(20).insert_at_end(30).insert_at_end(
        40
    ).display().revers_ll().display()
    link_list_head.insert_at_end(10).insert_at_end(20).insert_at_end(
        30
    ).display().insert_at_start(0).display().insert_at_index(
        0, -1
    ).display().insert_at_index(
        5, 40
    ).display().insert_at_index(
        2, 5
    ).display().delete_by_value(
        30
    ).display().find_index(
        40
    ).revers_ll().display()
