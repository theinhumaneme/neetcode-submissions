class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = {}
        _max = 0
        for v in nums:
            if v not in c.keys():
                c[v] = 1
            else:
                c[v] += 1

        for key in c.keys():
            sl = 1
            if key - 1 in c.keys():
                continue
            else:
                val = key + 1
                while val in c.keys():
                    sl += 1
                    val += 1
                _max = max(_max, sl)
        return _max
