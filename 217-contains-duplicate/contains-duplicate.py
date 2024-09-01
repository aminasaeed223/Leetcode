class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for n in nums:
            if n in mydict:
                return True
            mydict[n] = True
        return False
        
        