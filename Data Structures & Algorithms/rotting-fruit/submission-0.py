class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0
        rotten = deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.append((r, c))

        if len(rotten) < 1 and fresh > 0:
            return -1
        if len(rotten) < 1 and fresh == 0:
            return 0

        while rotten and fresh > 0:

            l = len(rotten)
            minutes += 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for _ in range(l):
                row, col = rotten.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or grid[r][c] == 2:
                        continue

                    grid[r][c] = 2
                    fresh -= 1
                    rotten.append((r, c))
                    

        return minutes if fresh == 0 else -1