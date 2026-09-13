class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                v2 = int(stack.pop())
                v1 = int(stack.pop())
                stack.append((v1 + v2))
            elif t == '-':
                v2 = int(stack.pop())
                v1 = int(stack.pop())
                stack.append((v1 - v2))
            elif t == '*':
                v2 = int(stack.pop())
                v1 = int(stack.pop())
                stack.append((v1 * v2))
            elif t == '/':
                v2 = int(stack.pop())
                v1 = int(stack.pop())
                stack.append((v1 / v2))
            else:
                stack.append(t)
        return int(stack.pop())      