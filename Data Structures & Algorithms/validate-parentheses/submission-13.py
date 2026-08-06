class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}": "{", "]": "[", ")": "("}
        stack = []

        for ch in s:
            if ch in "{([":
                stack.append(ch)
            else:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False

