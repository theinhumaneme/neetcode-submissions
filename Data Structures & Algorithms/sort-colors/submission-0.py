class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        o = 0
        t = 0
        for i in nums:
            if i == 0:
                z+=1
            elif i == 1:
                o+=1
            elif i == 2:
                t+=1
        for _ in range(0,z):
            nums[_] = 0
        for _ in range(z,z+o):
            nums[_] = 1
        for _ in range(z+o,z+o+t):
            nums[_] = 2