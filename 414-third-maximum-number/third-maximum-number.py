class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # First we will convert nums into set
        new = set(nums)
        # Checking some conditions if len of nums is less than three it means 1,2 will be present only so, in this case we will return maximum number which is 2
        if len(new) < 3:
            return max(new)
        elif len(new) == 3:
            return min(new)
        # else in case we have to remove one by one
        else:
            new.remove(max(new))
            new.remove(max(new))
            return max(new)





        