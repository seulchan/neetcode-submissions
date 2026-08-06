class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}": "{", "]": "[", ")": "("}
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif stack and ch in "})]" and stack[-1] == closeToOpen[ch]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False