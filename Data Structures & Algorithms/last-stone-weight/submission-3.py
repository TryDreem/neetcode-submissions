class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)
        k = 2
        while len(h) > 1:
            curr = []
            for i in range(k):
                curr.append(heapq.heappop(h))

            diff = abs(curr[0] - curr[1])

            if diff > 0:
                heapq.heappush(h, -diff)
            
        return -h[0] if len(h) == 1 else 0

            

