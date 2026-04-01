class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []

        def backtrack( open_N, closed_N):
            if open_N == closed_N == n:
                res.append("".join(stack))
                return
            
            if open_N < n:
                stack.append("(")
                backtrack(open_N + 1, closed_N)
                stack.pop()
            
            if closed_N < open_N:
                stack.append(")")
                backtrack(open_N, closed_N + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res