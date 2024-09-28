class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()
        reversed_words = words[::-1]
        s = ' '.join(reversed_words)
        return s