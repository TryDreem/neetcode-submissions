class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        r1, r2 = 0, 0

        for i in range(len(nums) - 1):
            tmp = max(r1 + nums[i], r2)
            r1 = r2
            r2 = tmp
        
        res1 = r2

        r3, r4 = 0, 0

        for j in range(len(nums) - 1, 0, -1):
            tmp = max(r3 + nums[j], r4)
            r3 = r4
            r4 = tmp

        res2 = r4
        
        return max(res1, res2)
