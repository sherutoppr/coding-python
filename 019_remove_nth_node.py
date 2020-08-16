'''Given a linked list, remove the n-th node from the end of list and return its head.'''


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        first, second = head, head
        for i in range(n):
            first = first.next

        if not first:
            return head.next

        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next

        return head


