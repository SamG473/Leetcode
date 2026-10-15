class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()       
        start = 0            
        longest = 0

        for right in range(len(s)): 
            letter = s[right]

            
            while letter in seen:
                seen.remove(s[start])
                start += 1

            
            seen.add(letter)

           
            window_length = right - start + 1
            if window_length > longest:
                longest = window_length

        return longest
