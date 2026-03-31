def to_sum(arr,target):
    left =0
    right=len(arr)-1

    while left < right:
        current=arr[left]+arr[right]

        if current==target:
            return [left+1], [right+1]
        
        elif current < target:
             left +=1

        else:
             right -=1
