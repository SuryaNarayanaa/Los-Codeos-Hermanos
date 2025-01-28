def threeSum( nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i+1
            r = len(nums)-1
            
            while(l<r):

                s = nums[i] + nums[l] + nums[r]
                
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    print(ans)
                    # Skip duplicates for l
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # Skip duplicates for r    
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    
        return ans

print(threeSum([-1,0,1,2,-1,-4]))