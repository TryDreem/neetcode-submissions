class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for ele in nums:
            if ele - 1 not in nums:
                curr_max = 1
                i = 1
                while ele + i in nums:
                    curr_max += 1
                    i += 1
                res = max(curr_max, res)
        return res

                

