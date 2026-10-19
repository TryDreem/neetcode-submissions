class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [ [] for i in range(len(nums) + 1) ]
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        for ele, c in counts.items():
            freq[c].append(ele)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for ele in freq[i]:
                res.append(ele)
                if len(res) == k:
                    return res
