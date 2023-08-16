from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parenMap = { ')' : '(', ']' : '[', '}' : '{'}
        

        for paren in s:
            # if parethese is an open parethese
            if paren in parenMap.values():
                stack.append(paren)
            else:
                if len(stack) > 0 and stack[len(stack) - 1] ==  parenMap[paren]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
