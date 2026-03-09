# Problem 8 - Merge Two Sorted Arrays
# Given two sorted arrays, merge them into one sorted array
# Example: [1, 3, 5] and [2, 4, 6] → [1, 2, 3, 4, 5, 6]



def merge_sorted(arr1, arr2):
    return sorted(arr1 + arr2)


print(merge_sorted([1,3,5], [2,4]))