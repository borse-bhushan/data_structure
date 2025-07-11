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

    def insert_at_end(self, data):

        if self.head is None:
            self.head = Node(data)
            self.head.next_node = self.head
            return self

        current = self.head
        while current.next_node != self.head:
            current = current.next_node

        new_node = Node(data)
        current.next_node = new_node
        new_node.next_node = self.head

        return self

    def display(self):
        node = self.head

        result = []
        while node:

            node_data = f"{str(node)}"
            result.append(node_data)

            node = node.next_node

        str_pr = " -> ".join(result)

        str_2 = ""
        str_pr_len = len(str_pr)
        for ind in range(str_pr_len):
            if ind == 0:
                str_2 += "|"
            elif ind == (str_pr_len - 1):
                str_2 += "|"
            else:
                str_2 += "_"
        str_pr += "\n"
        str_pr += str_2

        print(str_pr)

        return self


if __name__ == "__main__":

    LinkList().insert_at_end(10).insert_at_end(20).insert_at_end(30).display()
