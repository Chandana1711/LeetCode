class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join(char.lower() for char in s if char.isalnum())
        rev_str = new_str[::-1]
    
        return new_str == rev_str
