class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sorted(s)
        b = sorted(t)
        
        for i in range(len(a)):
            if a[i] != b[i]:
                return b[i]
        
        return b[-1]
        