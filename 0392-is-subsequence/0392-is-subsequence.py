class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        j = 0
        for i in range(len(s)):
            while j<len(t) and t[j] != s[i]:
                j+=1
                
            if j == len(t):
                return False
            
            j += 1
            count += 1
                
    
        return count == len(s)