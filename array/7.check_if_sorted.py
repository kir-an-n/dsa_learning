# Problem 7 - Check if Sorted
# Given an array, return True if sorted in ascending order, False if not
# Example: [1, 2, 3, 4, 5] → True
# Example: [1, 3, 2, 4, 5] → False



def check_if_sorted(arr):
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
        
    return True
print(check_if_sorted([2,3,4,6,5]))