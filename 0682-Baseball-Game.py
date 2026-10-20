class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = [] 

        for operation in operations:  
            
            if operation == '+': 
                new = (stack[-1] + stack[-2])
                stack.append(new)
            elif operation == 'D': 
                double = stack[-1] * 2
                stack.append(double)
            elif operation == 'C' and len(stack) != 0:
                stack.pop()
            else: 
                stack.append(int(operation))

        return sum(stack) 
