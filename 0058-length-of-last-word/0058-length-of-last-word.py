class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        
        my_list = s.strip().split(' ')
        if my_list:
            last_word = my_list[-1]
            return len(last_word)    
        
        