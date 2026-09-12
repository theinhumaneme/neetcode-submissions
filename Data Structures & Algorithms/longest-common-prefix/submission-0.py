class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final = ""
        strs = sorted(strs)
        f = strs[0]
        l = strs[len(strs)-1]
        for i in range(min(len(f), len(l))):
            if f[i] == l[i]:
                final+= f[i]
            else:
                break
        return final
        