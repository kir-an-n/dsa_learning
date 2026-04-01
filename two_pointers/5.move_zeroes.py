def move_zeroes_to_end(nums):
    slow=0

    for fast in range(len(nums)):
        if nums[fast] !=0:
            nums[slow] = nums[fast]
            slow += 1
      
    for  i in range(slow, len(nums)):
        nums[i]=0

        
    return nums


print(move_zeroes_to_end([0,1,0,3,12]))