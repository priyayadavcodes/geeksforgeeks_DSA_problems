class Solution:
    def nonRepeatingChar(self, s):
        freq = {}
        
        # 1️⃣ Count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # 2️⃣ Find first character with count == 1
        for ch in s:
            if freq[ch] == 1:
                return ch
        
        return '$'
