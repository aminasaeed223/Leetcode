class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)/2
        a = list(set(nums))
        for i in a:
            c = nums.count(i)
            if(c>n):
                return i 
        
        