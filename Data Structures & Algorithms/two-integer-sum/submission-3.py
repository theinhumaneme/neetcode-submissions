class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        for i in range(0, len(nums)):
            _val = target - nums[i]
            if _val in nums[i+1:]:
                return [i, nums.index(_val, i + 1)]