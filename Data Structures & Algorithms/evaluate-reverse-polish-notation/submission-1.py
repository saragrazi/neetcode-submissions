class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "/", "*", "-"}
        for elem in tokens:
            if elem in operators:                    
                b = stack.pop()
                a = stack.pop()
                if elem == "+":
                    stack.append(a+b)
                if elem == "-":
                    stack.append(a-b)
                if elem == "*":
                    stack.append(a*b)
                if elem == "/":
                    stack.append(int(a/b))
            else:
                stack.append(int((elem)))
        return stack[0]
            




        
        