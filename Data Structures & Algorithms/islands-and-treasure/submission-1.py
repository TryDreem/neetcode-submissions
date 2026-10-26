class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dist = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            dist += 1
            qLen = len(q)
            for i in range(qLen):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == 2147483647:
                        grid[r][c] = dist
                        q.append((r, c))
	
	
