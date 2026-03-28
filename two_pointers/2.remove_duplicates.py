#remove duplicates

def remove_duplicates(nums):
    if not nums:
        return 0
    
    left=0
    
    for right in range(1,len(nums)):
        if nums[right] != nums[left]:
            left +=1
            nums[left]=nums[right]
        
    return 
# Test
nums = [1, 1, 2, 2, 3]
length = remove_duplicates(nums)
print(length)        # Should print 3
print(nums[:length]) # Should print [1, 2, 3]






