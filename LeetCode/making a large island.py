

def largestIsland( grid):
    r,c = len(grid), len(grid[0])
    visited = [[False]*c for _ in range(r)]
    hmap = {}
    def dfs(i,j, f):
        if i<0 or i>=r or j<0 or j>=c or visited[i][j] or grid[i][j] == 0 :
            return 0
        visited[i][j]  = True
        grid[i][j] = f
        directions =         [(0, 1), (1, 0), (0, -1), (-1, 0)]
         
        cnt = 1
        for dx, dy in directions:
           cnt+= dfs(i+dx , j+dy , f)
        hmap[f] =cnt
        return cnt
    maxi = 0
    f= 2
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and grid[i][j] ==1:
                
                max_dfs = dfs(i,j ,f)
                f+=1
                maxi = max(maxi, max_dfs)

    for i in range(r):
        for j in range(c):
            if grid[i][j] ==0 :
                size =1
                seen = set()
                directions =         [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0<= ni<r and 0<=nj<c and grid[ni][nj] > 1:
                        seen.add(grid[ni][nj])
                for islands in seen:
                    size+= hmap[islands]
                maxi = max(maxi , size)

    return maxi




            


grid = [
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 1, 1]
]
# Call the function with the 4 by 4 matrix
print(largestIsland(grid))
print(grid)
