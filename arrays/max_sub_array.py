# A subarray is a contiguous part of array.
#  An array that is inside another array. 
# For example, consider the array [1, 2, 3, 4],
#  There are 10 non-empty sub-arrays. The subarrays are (1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4) and (1,2,3,4). In general, for an array/string of size n, there are n*(n+1)/2 non-empty subarrays/substrings.


# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def sub_array(arr):
    
    # spread the given array
    sub_arrys = [[i] for i in arr]
    highest_array = [i for i in arr]

    # construct the subarray
    for i in range(len(arr)):
        left_arr = arr[i+1:]
        counter = 1

        for j in range(len(left_arr)):
            sub_arrys.append([arr[i]] + left_arr[:counter])
            highest_array.append(sum([arr[i]]+ left_arr[:counter]))
            counter += 1

    #

    
    highest_array.sort(reverse=True)
    return sub_arrys, highest_array


test=[1,2,3,4]
test2=[-2,1,-3,4,-1,2,1,-5,4]

_,high_arr = sub_array(test)
_,high_arr2 = sub_array(test2)

print(high_arr[0])
print(high_arr2[0])



