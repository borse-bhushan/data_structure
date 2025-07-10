from singly_linked_list import LinkList, Node


def add_two_numbers(l1: LinkList, l2: LinkList):

    l1.revers_ll().display()
    l2.revers_ll().display()

    l1_node = l1.head
    l2_node = l2.head

    carry = 0
    new_ll = LinkList()

    while l1_node or l2_node:

        l1_val = l1_node.data if l1_node else 0
        l2_val = l2_node.data if l2_node else 0

        digit = (l1_val + l2_val + carry) % 10
        carry = (l1_val + l2_val + carry) // 10

        new_ll.insert_at_start(digit)

        if l1_node:
            l1_node = l1_node.next_node

        if l2_node:
            l2_node = l2_node.next_node

    if carry != 0:
        new_ll.insert_at_start(carry)

    new_ll.display()


if __name__ == "__main__":
    l1 = LinkList().insert_at_end(2).insert_at_end(4).insert_at_end(3)
    l2 = LinkList().insert_at_end(5).insert_at_end(6).insert_at_end(4)

    add_two_numbers(l1, l2)
