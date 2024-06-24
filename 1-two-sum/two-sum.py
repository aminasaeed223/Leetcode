class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map = {}
        # for i , num in enumerate(nums):
        #     if target-num in hash_map:
        #         return [hash_map[target-num],i]
        #     hash_map[num] = i
        # return hash_map
        new = len(nums)
        for i in range(new):
            for j in range(i+1, new):
                if nums[i] + nums[j] == target:
                   return [i, j]
        return []

            
        