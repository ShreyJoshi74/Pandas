class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        queue = deque()
        n = len(grid)
        vis = [[False for _ in range(n)] for _ in range(n)] 
        time = [[2 ** 31 for _ in range(n)] for _ in range(n)]
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        queue.append([0,0,grid[0][0]])
        time[0][0] = grid[0][0]
        while queue:
            current = queue.popleft()
            currentTime = current[2]
            i = current[0]
            j = current[1]

            for dirr in direction:
                ni = i + dirr[0]
                nj = j + dirr[1]
                if(ni >= 0 and ni < n and nj >= 0 and nj < n and time[ni][nj] > max(currentTime , grid[ni][nj])):
                    time[ni][nj] = max(currentTime,grid[ni][nj])
                    queue.append([ni,nj,time[ni][nj]])
                    
        return time[n-1][n-1]





