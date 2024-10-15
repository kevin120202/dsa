class Solution(object):
    def isPalindrome(self, s):
        new_string = ""
        for c in s:
            if c.isalnum():
                new_string += c.lower()
        start = 0
        end = len(new_string) - 1
        while start < end:
            if new_string[start] != new_string[end]:
                return False
            start += 1
            end -= 1
        return True
