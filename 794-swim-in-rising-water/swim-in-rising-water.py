import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = [[False for _ in range(n)] for _ in range(n)]
        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        # Min-heap: (time, i, j)
        pq = [(grid[0][0], 0, 0)]  
        vis[0][0] = True
        time = 0

        while pq:
            t, i, j = heapq.heappop(pq)
            time = max(time, t)
            
            # reached destination
            if i == n-1 and j == n-1:
                return time
            
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and not vis[ni][nj]:
                    vis[ni][nj] = True
                    heapq.heappush(pq, (grid[ni][nj], ni, nj))
        
        return time
