# Solution for LeetCode problem: Merge Sorted Array

def solution():
    """
    Merge Sorted Array (LeetCode 88).
    Usage: Call merge(nums1, m, nums2, n) where nums1 and nums2 are lists, m and n are their valid lengths.
    Modifies nums1 in-place to be the merged sorted array.
    """
    def merge(nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    # Example usage:
    # nums1 = [1,2,3,0,0,0]
    # nums2 = [2,5,6]
    # merge(nums1, 3, nums2, 3)
    # print(nums1) # Output: [1,2,2,3,5,6]
    pass
