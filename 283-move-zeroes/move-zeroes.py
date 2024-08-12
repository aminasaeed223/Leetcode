class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using two pointer approach
        left = 0 #it will keep track of zeros
        for right in range(len(nums)):
            if nums[right] != 0:
                # swap
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
            
   
        
        