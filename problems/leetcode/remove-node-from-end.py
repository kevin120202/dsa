def removeNthFromEnd(self, head, n):
    dummy = ListNode(0, head)
    left_ptr = dummy
    right_ptr = head

    for _ in range(n):
        right_ptr = right_ptr.next

    while right_ptr:
        right_ptr = right_ptr.next
        left_ptr = left_ptr.next

    left_ptr.next = left_ptr.next.next
    return dummy.next
