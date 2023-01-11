



# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# input
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


def two_sum(arr , tar ):
    out_put = []

    for num in range(len(arr)):
        for j in arr[num+1:]:
            if arr[num] +  j == tar:
                out_put.append(num)

    return(out_put)


nums = [ 2, 7, 11, 15,1,8]
target = 9
print(two_sum(nums, target))

