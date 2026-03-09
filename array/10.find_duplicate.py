# Problem 10 - Find Duplicate
# Given an array, find the number that appears more than once
# Example: [1, 2, 3, 2, 4] → 2



def find_duplicate(arr):
    seen=set()

    for x in arr:
        if x in seen:
            return x
        
        seen.add(x)

print(find_duplicate([1,2,3,4,4,5,6,7,8]))