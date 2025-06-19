# Solution for LeetCode problem: Remove Duplicates94

def solution():
    """
    Remove Duplicates from Sorted Array (LeetCode 26).
    Usage: Call removeDuplicates(nums) where nums is a List[int] sorted in non-decreasing order.
    The function returns the new length k, and modifies nums in-place so that the first k elements are unique.
    """
    def removeDuplicates(nums):
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k
    # Example usage:
    # nums = [1,1,2]
    # k = removeDuplicates(nums)
    # print(nums[:k]) # Output: [1, 2]
    pass
