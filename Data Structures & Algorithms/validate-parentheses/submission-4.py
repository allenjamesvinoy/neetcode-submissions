class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        res = True
        for c in s:
            if len(stack) == 0: 
                stack.append(c)
                continue

            val = stack[-1]
            match c:
                case ')':
                    if val != '(':
                        res = False
                    else:
                        stack.pop()
                case '}':
                    if val != '{':
                        res = False
                    else:
                        stack.pop()
                case ']':
                    if val != '[':
                        res = False
                    else:
                        stack.pop()
                case _:
                    stack.append(c)

            if not res:
                break

        return len(stack) == 0
            
