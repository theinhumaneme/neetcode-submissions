class Solution:
    def simplifyPath(self, path: str) -> str:
        values = path.split("/")
        o = []
        for val in values:
            if val == "":
                continue
            elif val == ".":
                continue
            elif val == "..":
                if len(o) != 0:
                    o.pop()
            else:
                o.append(val)
        return "/"+"/".join(o)