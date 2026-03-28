#Problem 2 — Find Max
#Loop through the array, keep track of the biggest number you've seen.


def find_max(arr):
    max_number=arr[0]
    for i in range(len(arr)):
        if arr[i] > max_number:
            max_number=arr[i]

    return max_number

print(find_max([3,3,3,3,2,1,7]))