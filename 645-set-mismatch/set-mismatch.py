class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # dup = -1
        # missing = -1
        # for i in range(1, len(nums) + 1):
        #     count = nums.count(i)
        #     if count == 2:
        #         dup = i
        #     elif count == 0:
        #         missing = i
        # return [dup, missing]

        

        n = len(nums)
        v = [0] * (n + 1)
        missing, duplicate = 0, 0

        for num in nums:
            v[num] += 1

        for i in range(1, len(v)):
            if v[i] == 2:
                duplicate = i
            if v[i] == 0:
                missing = i

        return [duplicate, missing]


        