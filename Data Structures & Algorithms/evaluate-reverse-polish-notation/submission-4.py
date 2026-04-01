import operator
# operator.add(a,b), operator.sub(a,b), operator.mul(a,b), operator.floordiv(a,b)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        ops = ["+","-","*","/"]
        for t in tokens:
            if t in ops:
                if t == ops[0]:
                    v = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(v)
                elif t == ops[1]:
                    v = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(v)
                elif t == ops[2]:
                    v = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(v)
                else:
                    v = int(float(stack[-2]) / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(v)
            else:
                stack.append(int(t))
        return stack[0]
        