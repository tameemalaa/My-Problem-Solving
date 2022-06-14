class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if not(stack):
                stack.append(i)
            elif i == "]":
                x = stack.pop()
                if x != "[":
                    return False
            elif i == "}":
                x = stack.pop()
                if x != "{":
                    return False
            elif i == ")":
                x = stack.pop()
                if x != "(":
                    return False
            else : 
                stack.append(i)
        return not(stack)