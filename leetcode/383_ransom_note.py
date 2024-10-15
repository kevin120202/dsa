class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        m_dict = {}
        for char in magazine:
            m_dict[char] = 1 + m_dict.get(char, 0)
        
        for char in ransomNote:
            if char not in m_dict or m_dict[char] <= 0:
                return False
            m_dict[char] -= 1
        
        return True