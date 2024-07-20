# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy_node = ListNode(1)
        current = dummy_node
        ptr1 = list1
        ptr2 = list2
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next
        if ptr1:
            current.next = ptr1
        if ptr2:
            current.next = ptr2
        return dummy_node.next
