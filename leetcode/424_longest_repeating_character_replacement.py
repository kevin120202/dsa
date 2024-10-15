class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # To keep track the freq of each char.
        freq = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            # Get the most freq letter in the string to check if the window is valid.
            most_freq = 0
            for key in freq:
                if freq[key] > most_freq:
                    most_freq = freq[key]

            sub_length = (r - l) + 1
            # Check if window is valid.
            if sub_length - most_freq <= k:
                res = max(res, sub_length)
            else:
                freq[s[l]] -= 1
                l += 1

        return res
