class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in seen: 
                return [i, seen[find]]
            seen[nums[i]] = i 
