class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a -> b (2)    b -> c (3)    a -> c (6)
        helper = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            helper[a].append([b, values[i]])
            helper[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in helper or target not in helper:
                return -1
            q = deque([[src, 1]])
            visited = set()
            visited.add(src)

            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, wei in helper[n]:
                    if nei not in visited:
                        q.append([nei, wei * w])
                        visited.add(nei)

            return -1

        return [bfs(q[0], q[1]) for q in queries]