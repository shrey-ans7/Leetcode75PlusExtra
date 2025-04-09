class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        # The difference between set1 and set2
        diff1 = list(set1 - set2)
        # The difference between set2 and set1
        diff2 = list(set2 - set1)
        
        return [diff1, diff2]
