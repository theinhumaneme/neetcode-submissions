class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fm = {}
        for n in nums:
            if n not in fm:
                fm[n] = 1
            else:
                fm[n] = fm[n]+1
        for x, y in fm.items():
            if y > (len(nums)/2):
                return x
        