def reverseList(head):
    previous = None
    current = head
    next = None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous
