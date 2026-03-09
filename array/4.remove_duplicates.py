# Problem 4 - Remove Duplicates
# Given an array, remove duplicate values
# Example: [1, 2, 2, 3, 4, 4, 5] → [1, 2, 3, 4, 5]



def remove_duplicates(arr):
    return list(set(arr))

print(remove_duplicates([1,2,3,4,2,4,5]))