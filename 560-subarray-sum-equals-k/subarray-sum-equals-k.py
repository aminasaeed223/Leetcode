class Solution:
    def subarraySum(self, nums, k):
        count = 0
        cumulative_sum = 0
        sum_map = {0: 1} 
        
        for num in nums:
            cumulative_sum += num 
            if cumulative_sum - k in sum_map:
                count += sum_map[cumulative_sum - k]  
            sum_map[cumulative_sum] = sum_map.get(cumulative_sum, 0) + 1  
        return count
        