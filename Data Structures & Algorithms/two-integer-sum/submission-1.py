class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for j in range(len(nums)):
            diff = target - nums[j]
            if diff not in seen:
                seen[nums[j]] = j
            else:
                return [seen[diff], j]
        