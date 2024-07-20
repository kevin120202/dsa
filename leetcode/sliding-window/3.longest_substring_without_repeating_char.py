class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substring = set()
        l = 0
        max_length = 0
        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length
