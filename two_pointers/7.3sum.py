def three_sum(arr,target):
    arr.sort()
    results=[]

    for i in range(len(arr)-1):
        left+=1
        right=len(arr)-1

        while left < right:
            current_sum=arr[i]+arr[left]+arr[right]
            if current_sum==target:
                results.append((arr[i], arr[left], arr[right]))
                left+=1
                right-=1
            elif current_sum<target:
                left+=1
            else:
                right-=1

    return results
