#Problem 1 — Reverse Array
#Two pointers, i and j, swap until they meet. You already explained it correctly earlier!


def reverse_array(arr):
    i=0
    j=len(arr)-1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

print(reverse_array([4,3,8,1]))