from urllib3 import Retry


def check( nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    k= 0
    fe=0 
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i] :
            if k==2:
                return False
            k+=1
        if k == 0 :
            return True
        if k==1 and nums[0] >  nums[len(nums)-1]:
            return True 
        return False
        
            

            # Example usage
nums =[7,9,1,1,1,3]
print(check(nums))  # Output should be True if the list is sorted and rotated, otherwise False

        
        

    