class Solution:
    def isPalindrome(self, x: int) -> bool:
        newstring = str(x)
        return newstring == newstring[::-1]
        