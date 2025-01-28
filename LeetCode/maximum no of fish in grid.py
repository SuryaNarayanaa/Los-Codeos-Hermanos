def findMaxFish( grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rows = len(grid)
    cols=  len(grid[0])


    visited = [[False]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
             if grid[i][j] == 0:
                  visited[i][j] = True
    def dfs(root, visited):
        x,y = root
        if x<0 or x>=rows  or y<0 or y>=cols or visited[x][y]:
            return 0
        directions = [(-1,0), (0,-1), (1,0) ,(0,1)]

        
        count = grid[x][y]
        visited[x][y] = True
        for dx, dy in directions:
            count+= dfs((x+dx , y+dy ), visited)
        return count


    max_fish= 0
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                max_fish = max(max_fish , dfs((i,j) ,visited ))
    return max_fish

grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
print(findMaxFish(grid))