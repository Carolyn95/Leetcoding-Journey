# missing number in an array
"""
Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N. Find the missing element.

Input:
N = 5
A[] = {1,2,3,5}
Output: 4

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
"""
# solution one
def MissingNumber(array,n):
    # code here
    array.sort()
    for i in range(1, n+1):
        try:

            if i != array[i-1]:
                return i
        except:
            return n

# solution two
def MissingNumber(array,n):
    # code here
    return sum(range(n+1)) - sum(array)
