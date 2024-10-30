class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for n in nums:
            if abs(n) < abs(closest):
                closest = n

        # Corrected line
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest