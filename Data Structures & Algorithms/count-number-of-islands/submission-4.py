class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            visited.add((r, c))
            q = deque([(r, c)])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row > rows - 1 or col > cols - 1 or grid[row][col] == "0" or (row, col) in visited:
                        continue
                    q.append((row, col))
                    visited.add((row, col))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.res += 1
                    bfs(r, c)
        return self.res


                    