class Node:
    def __init__(self, key, val):

        self.key = key
        self.val = val

        self.next: Node = None
        self.prev: Node = None


class LRUCache:

    def __init__(self, capacity):

        self.cache = {}
        self.capacity = capacity
        self.head: Node = None
        self.tail: Node = None

    def __insert_at_start(self, new_node: Node):

        new_node.prev = None
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def __delete_node(self, node: Node):
        prev = node.prev
        next = node.next

        if prev:
            prev.next = next
        else:
            self.head = node.next

        if next:
            next.prev = prev
        else:
            self.tail = node.prev

        node.next = node.prev = None

    def __setitem__(self, key, value):

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.__delete_node(node)
            self.__insert_at_start(node)

        else:
            if len(self.cache) == self.capacity:
                tail = self.tail
                self.__delete_node(tail)
                del self.cache[tail.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.__insert_at_start(new_node)

    def __getitem__(self, key):

        if key not in self.cache:
            raise KeyError(key)

        node: Node = self.cache[key]
        self.__delete_node(node)
        self.__insert_at_start(node)
        return node.val


cache = LRUCache(5)


cache["data"] = "asd"

print(cache["data"])
