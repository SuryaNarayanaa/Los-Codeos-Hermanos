
import re
from typing import List

def constructDistancedSequence(n: int) -> List[int]:
	
    ans = [0]*(2*n -1)
    def backtrack(index):
        if index  == len(ans):
              return True
        if ans[index]!= 0 :
              return backtrack(index+1)
        for  i in range(n,0,-1):
            if i == 1 :
                 if i not in ans :
                      ans[index] = i
                      if backtrack(index+1):
                           return True
                      ans[index] = 0 
        
            else:
                 if i not in ans and i+index < len(ans) and ans[index + i] == 0:
                      ans[index] = i
                      ans[index + i] = i
                      if backtrack(index+1):
                           return True
                      ans[index] = 0
                      ans[index + i] = 0
        return False
    backtrack(0)
    return ans
                      


	
result = constructDistancedSequence(5)
print(result)
    
    # if index == len(ans):
    #         return True
    #     if ans[index] != 0:
    #         return backtrack(index + 1)
    #     for x in range(n, 0, -1):
    #         if x == 1:
    #             if x not in ans:
    #                 ans[index] = x
    #                 if backtrack(index + 1):
    #                     return True
    #                 ans[index] = 0
    #         else:
    #             if x not in ans and index + x < len(ans) and ans[index + x] == 0:
    #                 ans[index] = x
    #                 ans[index + x] = x
    #                 if backtrack(index + 1):
    #                     return True
    #                 ans[index] = 0
    #                 ans[index + x] = 0
    #     return False

    # backtrack(0)
    # return ans
