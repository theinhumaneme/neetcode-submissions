class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        for i in nums:
            if i not in vals:
                vals.update({i: 1})
            else:
                print(vals)
                vals[i]= vals.get(i) + 1
        freq = sorted(list(vals.values()),reverse=True)[0:k]
        final = []
        for i,j in vals.items():
            if j in freq:
                final.append(i)
        return final
        