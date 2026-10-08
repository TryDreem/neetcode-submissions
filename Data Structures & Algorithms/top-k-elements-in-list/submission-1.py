class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1) ]

        for ele in nums:
            count[ele] = count.get(ele, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) -1, 0, -1):
            for ele in freq[i]:
                res.append(ele)
                if len(res) == k:
                    return res