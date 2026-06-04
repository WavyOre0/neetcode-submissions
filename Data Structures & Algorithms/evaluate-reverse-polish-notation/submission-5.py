class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                val = num1 + num2
                stack.append(val)
            elif token == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                val = num2 - num1
                stack.append(val)
            elif token == "*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                val = num1 * num2
                stack.append(val)
            elif token == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                val = num2 / num1
                stack.append(val)
            else:
                stack.append(int(token))
        return int(stack.pop())
        #[220