class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        final.append(math.prod(nums[1:]))
        for val in range(1, len(nums)):
            _rp = math.prod(nums[0:val])
            final.append(_rp*math.prod(nums[val+1:]))
        return final
            