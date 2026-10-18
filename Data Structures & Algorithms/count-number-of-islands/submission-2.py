class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            self.res += 1
            q = deque([(r, c)])
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))
                        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
        return self.res



                