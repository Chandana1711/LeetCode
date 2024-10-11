class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return None
        guess= x/2
        tolerance = 0.000001
        
        while abs(guess*guess - x) > tolerance:
            guess = (guess + x/guess)/2
            
        return floor(guess)