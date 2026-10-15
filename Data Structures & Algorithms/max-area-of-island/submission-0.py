class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c):
            nonlocal maxArea
            visited.add((r, c))
            q = deque([(r, c)])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            curr_max = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited):	
                        curr_max += 1
                        visited.add((r, c))
                        q.append((r, c))
            maxArea = max(maxArea, curr_max)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    bfs(r, c)

        return maxArea

        