from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()

        prev = head
        current = head
        while current is not None:

            if current.val in seen:
                prev.next = current.next
                current = prev.next
            else:
                seen.add(current.val)
                prev = current
                current = current.next


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

print("---BEFOR---")
temp = head
while temp is not None:
    print(temp.val)
    temp = temp.next

print("------\n\n")

Solution().deleteDuplicates(head)
print("------\n\n")

print("---AFTRE---")

temp = head
while temp is not None:
    print(temp.val)
    temp = temp.next
