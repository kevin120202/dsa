class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        first_half = head
        second_half = prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            else:
                first_half = first_half.next
                second_half = second_half.next

        return True
