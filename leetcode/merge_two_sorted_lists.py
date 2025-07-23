# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if not list1 and not list2:
            return

        if list1 and not list2:
            return list1

        if not list1 and list2:
            return list2

        head = merge_list = ListNode(None)

        while list1 and list2:

            if list1.val >= list2.val:
                merge_list.next = list2
                list2 = list2.next
            else:
                merge_list.next = list1
                list1 = list1.next

            merge_list = merge_list.next

        if list1:
            merge_list.next = list1

        if list2:
            merge_list.next = list2
        return head.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)


l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


Solution().mergeTwoLists(l1, l2)
