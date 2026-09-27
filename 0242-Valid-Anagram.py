class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s = {}
        char_count_t = {}

        for char in range(len(s)):
            if s[char] not in char_count_s: 
                char_count_s[s[char]] = 1 
            else:
                char_count_s[s[char]] += 1
        
        for char in range(len(t)):
            if t[char] not in char_count_t:
                char_count_t[t[char]] = 1 
            else: 
                char_count_t[t[char]] += 1
        
        if char_count_s == char_count_t:
            return True
        
        return False 
        
