

#  Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.


# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


def contains_duplicate(arr):
    if len(arr) == len(set(arr)):
        return False
    return True


nums = [1,1,1,3,3,4,3,2,4,2]
nums2 = [1,2,3]


print(contains_duplicate(nums))
print(contains_duplicate(nums2))
