class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        lo, hi = 0, m
        inf = float('inf')

        while lo <= hi:
            i = lo + (hi - lo) // 2
            j = half - i

            nums1_left = nums1[i - 1] if i > 0 else -inf
            nums1_right = nums1[i] if i < m else inf
            nums2_left = nums2[j - 1] if j > 0 else -inf
            nums2_right = nums2[j] if j < n else inf

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2:
                    return float(max(nums1_left, nums2_left))
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            
            if nums1_left > nums2_right:
                hi = i - 1
            else:
                lo = i + 1