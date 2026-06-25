class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (sum(nums) != sum(set(nums)) or len(nums) != len(set(nums)))
        