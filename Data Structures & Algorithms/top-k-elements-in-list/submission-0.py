class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        countE = {}

        for ele in nums:
            if ele not in countE:
                countE[ele] = 1
            else:
                countE[ele] += 1
        
        res = []

        for _ in range(k):
            key = max(countE, key=countE.get)
            res.append(key)
            del countE[key]
        
        return res