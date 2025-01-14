
def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
                if flowerbed[i] == 1 :
                    if (i-1 >= 0 and flowerbed[i-1] == 1) or (i+1<len(flowerbed) and flowerbed[i+1] ==1):
                        return False
                    if i-2>=0 and flowerbed[i-2] == 0 :
                        print(i ,'1')
                        n-=1
                    if i+2 <len(flowerbed) and flowerbed[i+2] ==0:
                        n-=1
                        
                        print(i , '2')

    return n

print(canPlaceFlowers([0], 1))
"""
Hints to solve the flowerbed planting problem:

1. The problem is to determine if n flowers can be planted in the flowerbed following these rules:
   - No two flowers can be adjacent
   - Each 1 represents a flower, 0 represents an empty plot

2. Key approach:
   - Iterate through the array
   - For each position i, check if you can plant a flower by verifying:
     * Current position is empty (flowerbed[i] == 0)
     * Previous position is empty or it's the first position
     * Next position is empty or it's the last position
   - If all conditions met, plant a flower (set to 1) and decrease n
   
3. Implementation tips:
   - Handle edge cases (empty array, n=0)
   - You can modify the input array while checking
   - Keep track of how many flowers you've planted
   - Return true if you can plant all n flowers

4. Example solution structure:
   count = 0
   for i in range(len(flowerbed)):
       if flowerbed[i] == 0 and
          (i == 0 or flowerbed[i-1] == 0) and
          (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
           flowerbed[i] = 1
           count += 1
   return count >= n
"""
