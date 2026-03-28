def two_pointer_opposite(arr,target):
    left=0
    right=len(arr)-1

    while left < right:
        current=arr[left] +arr[right]

        if current ==target:
            return [left+1, right+1]
        
        elif current < target:
            left +=1

        else:
            right-=1

    return []

print(two_pointer_opposite([2,7,11,15],9))
print(two_pointer_opposite([1,2,3,4],7))
print(two_pointer_opposite([1,2,3,4],10))
