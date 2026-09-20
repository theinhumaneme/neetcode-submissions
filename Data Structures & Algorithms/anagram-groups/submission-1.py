class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = {}
        for _ in strs:
            s = "".join(sorted(_))
            if s not in values.keys():
                values[s] = [_]
            else:
                values[s].append(_)
        return (list(values.values()))