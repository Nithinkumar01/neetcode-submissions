class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = nums1 + nums2

        result.sort()

        length = len(result)

        if length % 2 == 1:
            mid = length // 2
            return result[mid]

        else:
            mid = length // 2
            return (result[mid - 1] + result[mid]) / 2
