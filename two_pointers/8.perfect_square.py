def perfect_square(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        sqrt = int(current_sum ** 0.5)

        if sqrt * sqrt == current_sum:
            return True
        elif current_sum < sqrt * sqrt + sqrt + sqrt + 1:
            left += 1
        else:
            right -= 1

    return False
        



          
    
          