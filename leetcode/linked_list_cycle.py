class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        # visited_nodes = {}
        # curr = head
        # while curr:
        #     if curr not in visited_nodes:
        #         visited_nodes[curr] = curr
        #     else:
        #         if curr.next in visited_nodes:
        #             return True
        #     curr = curr.next
        # return False
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
