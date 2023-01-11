# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]


def rotate( nums, k):

    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    rotated_arr = nums[len(nums)-k:]
    return rotated_arr + nums[:len(nums)-k]


nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))