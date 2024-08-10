class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
            # in case any negative number comes
        s = str(x)
        left = 0
        right = len(s) -1 
        while left < right:
            if s[left] != s[right]:
                return False
            right -=1
            left +=1
        return True
        