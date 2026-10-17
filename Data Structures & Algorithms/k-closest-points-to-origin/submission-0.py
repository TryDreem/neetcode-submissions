class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for ele in points:
            x, y = ele[0], ele[1]
            d = x**2 + y**2
            ele.insert(0, d)

        heapq.heapify(points)

        res = []

        for i in range(k):
            res.append(heapq.heappop(points)[1:])

        return res