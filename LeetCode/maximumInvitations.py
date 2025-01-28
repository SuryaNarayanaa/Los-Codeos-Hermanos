

def maximumInvitations(favorite):
    """
    :type favorite: List[int]
    :rtype: int
    """
    visited = [0]*len(favorite) 
        
    def dfs(root, degree ):
        nonlocal visited
        if degree == 0:
            visited = [0]*len(favorite)

        
        if visited[root] ==0 :
            
            visited[root] +=1
            return dfs( favorite[root] , degree+1)
        
        return  degree
    max_is = 0
    for i in range(len(favorite)):
        if visited[i] ==0 :
            max_is = max( max_is, dfs(i, 0))
    return max_is






favorite =[3,0,1,4,1]



print(maximumInvitations(favorite))