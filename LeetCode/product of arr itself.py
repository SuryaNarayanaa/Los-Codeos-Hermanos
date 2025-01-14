def productExceptSelf( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    first = float('inf')
    second = float('inf')
    
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
            
    return False

print(productExceptSelf([1,2,3,4,5]))
