class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums): #[-4, -1, -1, 0, 1, 2]
            if n == nums[i - 1] and i > 0:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = n + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

        return res

