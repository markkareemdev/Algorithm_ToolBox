# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Input
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]



def move_zero(arr):
    
    zeros_arr = []
    norm_arr =[]

    for num in arr:
        if num==0:
            zeros_arr.append(num)
        else:
            norm_arr.append(num)

    return norm_arr + zeros_arr
    

test = [0,1,0,3,12]
print(move_zero(test))