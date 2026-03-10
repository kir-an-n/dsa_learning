# Problem 9 - Find Pairs with Sum
# Given an array and target, find all pairs that add up to target
# Example: [1, 2, 3, 4, 5] target = 6 → [(1, 5), (2, 4)]


def find_pairs(arr, target):
    pairs=[]

    for i in range(len(arr)):
        complement=target - arr[i]

        if complement in arr and complement != arr[i]:

            if (complement, arr[i]) not in pairs:
                 pairs.append((arr[i], complement))

    return pairs
            
print(find_pairs([1,2,3,4,5,6,7,8,9], 11))


#we can do it by eihter complement or two pointers...........kirna stop misxing it up