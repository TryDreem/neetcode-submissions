class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = []
        q = deque()
        res = 0

        counts = Counter(tasks)

        for ele in counts.values():
            h.append(ele)

        h = [-ele for ele in h]

        heapq.heapify(h)

        while h or q:
            res += 1
            if h:
                count = 1 + heapq.heappop(h)
                if count:
                    q.append([count, res + n])
            if q and q[0][1] == res:
                tmp = q.popleft()
                heapq.heappush(h, tmp[0])

        return res



