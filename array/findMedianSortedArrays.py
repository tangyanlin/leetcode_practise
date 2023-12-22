class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        left = int((m+n+1)/2)
        right = int((m+n+2)/2)
        return (self.get_kth(nums1, 0, n - 1, nums2, 0, m - 1, left) + self.get_kth(nums1, 0, n - 1, nums2, 0, m - 1, right)) * 0.5
    
    def get_kth(self, nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
            return self.get_kth(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2 + k -1]
        
        if k == 1:
            return min(nums1[start1], nums2[start2])
        
        i = start1 + min(len1, int(k / 2)) - 1
        j = start2 + min(len2, int(k / 2)) - 1

        if nums1[i] > nums2[j]:
            return self.get_kth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.get_kth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))