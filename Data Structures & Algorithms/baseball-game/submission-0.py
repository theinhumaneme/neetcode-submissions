class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for _ in operations:
            if _ == "+":
                s.append(s[len(s) - 1]+s[len(s) - 2])
            elif _ == "C":
                s.pop()
            elif _ == "D":
                s.append(2*s[-1])
            else:
                s.append(int(_))
        return sum(s)
        