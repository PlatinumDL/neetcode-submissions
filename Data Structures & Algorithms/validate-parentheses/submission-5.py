class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        #Initialize Stack
        for i in range(len(s)):
            if s[i] == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif s[i] == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            elif s[i] == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        
        if len(stack) > 0:
            return False
        else:
            return True
