while left <=right:
        mid= (left + right) //2
        r=mid // cols
        c=mid % cols
        
        val=matrix[r][c]
        
        if val ==target:
            return True
            
        elif val< target:
            left=mid+1
            
        else:
            right=mid-1
            
    return False



