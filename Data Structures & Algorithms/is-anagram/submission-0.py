class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = {}, {}
        for c in list(s):
            if c in a.keys():
                a[c] = a[c]+1
            else:
                a[c]=1
        for c in list(t):
            if c in b.keys():
                b[c] = b[c]+1
            else:
                b[c]=1 
        
        if len(a.keys()) != len(b.keys()):
            return False

        for c in list(a.keys()):
            if a.get(c) == b.get(c):
                continue
            else:
                return False
        return True