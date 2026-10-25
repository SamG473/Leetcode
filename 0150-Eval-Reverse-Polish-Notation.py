class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []


        for operations in tokens: 

            if operations == '+':
                new = (stack[-2] + stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new)
            elif operations == '*': 
                new = (stack[-2] * stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new)
            elif operations == '-': 
                new = (stack[-2] - stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new)
            elif operations == '/': 
                new = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new)
            else: 
                stack.append(int(operations))
        
        return stack[0]
            
            
        
