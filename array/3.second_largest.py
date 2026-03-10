# Problem 3 - Find Second Largest
# Given an array, find the second largest number
# Example: [1, 5, 3, 9, 2] → 5


def second_largest(arr):
 
    if len(arr)< 2:     #check if we have enough numbers
        return None
    
    largest = float('-inf') #start both as the smallest possible value
    second = float('-inf')
     
    for num in arr:
        if num > largest:
            # The old largest is now the runner-up
            second = largest
            largest = num
        elif num > second and num != largest:
            # New runner-up found
            second = num
    
print(second_largest([1,5,3,9,2]))



#for single elmeent 
def find_ranks(arr):
    if not arr:
        return None
    
    # Initialize with the first element
    largest = arr[0]
    second = float('-inf') # Placeholder for "nothing yet"

    for i in range(1, len(arr)):
        if arr[i] > largest:
            second = largest
            largest = arr[i]
        elif arr[i] > second:
            second = arr[i]
    
    # If 'second' never changed, it means there was only one unique number
    if second == float('-inf'):
        return largest 
        
    return second