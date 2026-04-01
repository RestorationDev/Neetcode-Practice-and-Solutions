class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"}": "{", "]": "[", ")": "("}
        
        for char in s:
            if char in mapping:
                if not stack or mapping[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                print(stack)
                stack.append(char)
        return len(stack) == 0