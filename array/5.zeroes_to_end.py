# Problem 5 - Move Zeros to End
# Given an array, move all zeros to the end
# Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]


def move_zeros(arr):
    non_zeros=[x for x in arr if x!=0]
    zeros=[0] * (len(arr) -len(non_zeros))

    return non_zeros +zeros