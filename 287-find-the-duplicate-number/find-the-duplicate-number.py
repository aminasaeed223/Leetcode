class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_track = set()
        for i in nums:
            if i in set_track:
                return i 
            set_track.add(i)
        return -1
        