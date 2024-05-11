class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        if nums1.intersection(nums2):
            return min(nums1.intersection(nums2))
        return -1