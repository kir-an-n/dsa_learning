# Problem 3 - Find Second Largest
# Given an array, find the second largest number
# Example: [1, 5, 3, 9, 2] → 5


def second_largest(arr):
    largest=arr[1]
    second_largest=0
    
    for i in range(len(arr)-1):
        if arr[i] > largest:
            second_largest=largest
            largest=arr[i]
        elif arr[i]> second_largest:
            second_largest=arr[i]
    
    return second_largest

print(second_largest([1,5,3,9,2]))