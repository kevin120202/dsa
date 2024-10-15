class Solution(object):
    def maxNumberOfBalloons(self, text):
        freq = {}
        for char in text:
            freq[char] = 1 + freq.get(char, 0)
        
        res = 0
        while ("b" in freq and freq["b"] > 0 and 
                "a" in freq and freq["a"] > 0 and
                "l" in freq and freq["l"] > 1 and
                "o" in freq and freq["o"] > 1 and
                "n" in freq and freq["n"] > 0):
                    res += 1
                    freq["b"] -= 1
                    freq["a"] -= 1
                    freq["l"] -= 2
                    freq["o"] -= 2
                    freq["n"] -= 1
        return res