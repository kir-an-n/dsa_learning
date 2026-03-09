# Problem 6 - Find Missing Number
# Given an array of n-1 numbers from 1 to n, find the missing one
# Example: [1, 2, 3, 5] → 4



def find_missing_number(arr):
    n=len(arr)+1

    expected_sum=n*(n+1)//2
    actual_sum=sum(arr)
    return  expected_sum - actual_sum

print(find_missing_number([1,2,3,5]))  # should give 4


#thissoultion works only fir sorted arrays and arry that starts with 1 and it give sonly one missing number